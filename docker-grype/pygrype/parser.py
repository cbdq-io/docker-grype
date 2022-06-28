"""File: pygrype/parser.py."""
import json
import logging
import sys

from pygrype.vulnerabilities import Vulnerabilities
from pygrype.vulnerability import Vulnerability
from pygrype.vulnerabilities import severity_name_to_level


class ParseGrypeJSON():
    """Parse the JSON output from Anchore Grype."""

    def __init__(self, params):
        """
        Create a ParseGrypeJSON object.

        Parameters
        ----------
        params : pygype.params.Params
            The runtime parameters as gathered from the environment.
        """
        self._filename = None
        self._only_fixed = None
        self._max_severity_level = 0

        self.params = params

    def analyse_a_vulnerability(self, artifact, matched_vulnerability):
        """
        Analyse a matched vulnerability.

        If important, return the vulnerability otherwise return None.

        Parameters
        ----------
        artifact : dict
            A dictionary representing the artifact.
        matched_vulnerability : dict
            A dictionary representing a single vulnerability.

        Returns
        -------
        pygrype.vulnerability.Vulnerability
            The vulnerability or None of it doesn't qualify.
        """
        vulnerability_name = artifact['name']
        vulnerability_installed = artifact['version']
        vulnerability_id = matched_vulnerability['id']
        vulnerability_severity = matched_vulnerability['severity']
        level = severity_name_to_level(vulnerability_severity)
        allowed = self.is_vulnerability_allowed(vulnerability_id)
        add_vulnerability = self.params.show_all_vulnerabilities

        if level > self.params.tolerance_level and not allowed:
            add_vulnerability = True
            self.max_severity_level(level)

        if add_vulnerability:
            vulnerability = Vulnerability(vulnerability_id)
            vulnerability.name(vulnerability_name)
            vulnerability.installed_version(vulnerability_installed)
            vulnerability.severity(vulnerability_severity)
            vulnerability.allowed(allowed)
            return vulnerability

        return None

    def analyse_grype_data(self, grype_data):
        """
        Analyse the Grype data for vulnerabilities.

        Parameters
        ----------
        grype_data : dict
            The JSON file parsed into a dict.

        Returns
        -------
        tuple
            A list of Vulnerabilities.
            A list of allowed vulnerabilities that were not found in the scan.
        """
        vulnerabilities = Vulnerabilities(self.params)

        logging.debug(
            f'Tolerance is {self.params.tolerance_name} '
            + f'({self.params.tolerance_level})'
        )
        logging.debug(f"Grype version {grype_data['descriptor']['version']}")
        self.only_fixed()

        for match in grype_data['matches']:
            artifact = match['artifact']
            matched_vulnerability = match['vulnerability']
            vulnerability = self.analyse_a_vulnerability(artifact, matched_vulnerability)

            if not vulnerability:
                continue

            vulnerabilities.add(vulnerability)

        return vulnerabilities

    def collect_data(self):
        """
        Collect the Grype data from a file or stdin.

        Returns
        -------
        dict
            The parsed JSON data.
        """
        filename = self.filename()

        if filename:
            stream = open(filename)
            grype_data = json.load(stream)
            stream.close()
        else:
            grype_data = json.load(sys.stdin)

        return grype_data

    def filename(self, filename=None):
        """
        Get/set the filename.

        Parameters
        ----------
        filename : str, optional
            The name of the file to be parsed.

        Returns
        -------
        str
            The name of the file to be parsed.
        """
        if filename is not None:
            logging.debug(f'Set filename to {filename}')
            self._filename = filename

        return self._filename

    def is_vulnerability_allowed(self, vulnerability_id):
        """
        Check if a vulnerability ID is in the allowed list.

        Parameters
        ----------
        vulnerability_id : str
            The vulnerability id (e.g. CVE-000-0000).

        Returns
        -------
        bool
            True if the ID is found in the allowed list.
        """
        if vulnerability_id in self.params.vulnerabilities_allowed:
            allowed = True
        else:
            allowed = False

        return allowed

    def max_severity_level(self, max_severity_level=None):
        """
        Set the maximum severity level.

        Parameters
        ----------
        max_severity_level : int
            If this value is set to a value higher than any previous value
            set, this value becomes the new value.

        Returns
        -------
        int
            The maximum severity value found during the parsing.
        """
        if max_severity_level is not None:
            if max_severity_level > self.max_severity_level():
                self._max_severity_level = max_severity_level

        return self._max_severity_level

    def only_fixed(self):
        """
        Check if we be looking for only fixed vulnerabilities.

        Returns
        -------
        bool
            True of only flagging fixed vulnerabilities.  False if checking all vulnerabilities.
        """
        if self._only_fixed is not None:
            return self._only_fixed

        if self.params.only_fixed:
            mesg = 'Only fixed vulnerabilities will be searched for.'
            self._only_fixed = True
        else:
            self._only_fixed = False
            mesg = 'All vulnerabilities (fixed or not) will be searched for.'

        logging.debug(mesg)
        return self._only_fixed

    def report(self):
        """
        Create a report of the non-tolerated vulnerabilities.

        Returns
        -------
        int
            Zero if all vulnerabilities have a tolerance less than or equal to
            the specified tolerance.  Non-zero otherwise.
        """
        grype_data = self.collect_data()
        vulnerabilities = self.analyse_grype_data(grype_data)

        for vulnerability_id in vulnerabilities.missing_and_allowed():
            if vulnerability_id.strip():
                msg = f'"{vulnerability_id}" is in the allowed list '
                msg += 'but not found in the scan!'
                logging.warning(msg)

        print(vulnerabilities)
        logging.debug(
            f'Max severity level found was {self.max_severity_level()}.')

        if self.max_severity_level() <= self.params.tolerance_level:
            return 0
        else:
            return self.max_severity_level()
