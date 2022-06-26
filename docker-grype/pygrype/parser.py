"""File: pygrype/parser.py."""
import json
import logging
import os
import sys

from pygrype.vulnerabilities import Vulnerabilities
from pygrype.vulnerability import Vulnerability


class ParseGrypeJSON():
    """Parse the JSON output from Anchore Grype."""

    def __init__(self):
        """Create a ParseGrypeJSON object."""
        self._tolerance_name = None

        if 'TOLERATE' in os.environ:
            self.tolerance_name(os.environ['TOLERATE'])
        else:
            self.tolerance_name('Medium')

        self._max_severity_level = 0
        self._filename = None
        self._show_all = False
        self._only_fixed = None

        if 'SHOW_ALL_VULNERABILITIES' in os.environ:
            self.show_all(True)

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
        level = self.tolerance_name2level(vulnerability_severity)
        allowed = self.is_vulnerability_allowed(vulnerability_id)
        add_vulnerability = self.show_all()

        if level > self.tolerance_level() and not allowed:
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
        vulnerabilities = Vulnerabilities(self.show_all())
        unused_allowed_vulnerabilities = self.vulnerabilities_allowed_list()

        logging.debug(
            f'Tolerance is {self.tolerance_name()} '
            + f'({self.tolerance_level()})'
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

        for vulnerability in vulnerabilities.vulnerabilities:
            if vulnerability.vulnerability_id in unused_allowed_vulnerabilities:
                unused_allowed_vulnerabilities.remove(vulnerability.vulnerability_id)

        return vulnerabilities, unused_allowed_vulnerabilities

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
        if vulnerability_id in self.vulnerabilities_allowed_list():
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

        if 'ONLY_FIXED' in os.environ and os.environ['ONLY_FIXED'] == '1':
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
        (vulnerabilities, unused_allowed_vulnerabilities) = self.analyse_grype_data(grype_data)

        if len(unused_allowed_vulnerabilities):
            for vulnerability_id in unused_allowed_vulnerabilities:
                if vulnerability_id.strip():
                    msg = f'"{vulnerability_id}" is in the allowed list '
                    msg += 'but not found in the scan!'
                    logging.warning(msg)

        print(vulnerabilities)
        logging.debug(
            f'Max severity level found was {self.max_severity_level()}.')

        if self.max_severity_level() <= self.tolerance_level():
            return 0
        else:
            return self.max_severity_level()

    def show_all(self, show_all=None):
        """
        Get or set if we are to show all.

        Parameters
        ----------
        show_all : bool, optional
            Should all vulnerabilities be shown.

        Returns
        -------
        bool
            Should all vulnerabilities be shown.
        """
        if show_all is not None:
            self._show_all = show_all
        return self._show_all

    def tolerance_level(self, tolerance_level=None):
        """
        Get or set the tolerance level.

        Parameters
        ----------
        tolerance_level : int, optional
            The level of tolerance as an integer.

        Returns
        -------
        int
            Retuns the tolerance as an integer.
        """
        if tolerance_level is not None:
            self._tolerance_level = tolerance_level
        return self._tolerance_level

    def tolerance_name(self, tolerance_name=None):
        """
        Get or set the tolerance name.

        This will take the name and set to the tolerance level as well.

        Parameters
        ----------
        tolerance_name : str
            The tolerance name (e.g. CRITICAL).  Must match a value from valid_tolerance_names().

        Raises
        ------
            ValueError if the tolerance level is invalid.
        """
        if tolerance_name is not None:
            self._tolerance_name = tolerance_name.capitalize()

            if self._tolerance_name not in self.valid_tolerance_names():
                raise ValueError(f'Invalid tolerance level {tolerance_name}.')

            level = self.tolerance_name2level(
                tolerance_name.capitalize())
            self.tolerance_level(level)

        return self._tolerance_name

    def tolerance_name2level(self, tolerance_name):
        """
        Convert a tolerance name string to a tolerance level.

        Returns
        -------
        int
            An integer level representing the tolerance.
        """
        tolerance_names = self.valid_tolerance_names()

        for i in range(len(tolerance_names)):
            if tolerance_name == tolerance_names[i]:
                return i

        return 0

    def valid_tolerance_names(self):
        """
        Return a list of valid tolerance names.

        list of str
            A list of valid names in order of tolerance from 'Unknown' to
            'Critical'.
        """
        return [
                    'Unknown',
                    'Negligible',
                    'Low',
                    'Medium',
                    'High',
                    'Critical'
                ]

    def vulnerabilities_allowed_list(self):
        """
        Return the list of allowed vulnerabilities.

        Returns
        -------
        list of str:
            The list of allowed vulnerabilities.
        """
        if 'VULNERABILITIES_ALLOWED_LIST' in os.environ:
            return os.environ[
                'VULNERABILITIES_ALLOWED_LIST'
            ].split(',')
        else:
            return []
