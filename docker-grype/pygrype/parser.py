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
        if 'LOG_LEVEL' in os.environ:
            log_level = os.environ['LOG_LEVEL']
        else:
            log_level = 'INFO'

        logging.basicConfig(
            format='%(levelname)s:%(message)s',
            level=log_level)

        if 'TOLERATE' in os.environ:
            self.tolerance_name(os.environ['TOLERATE'])
        else:
            self.tolerance_name('Medium')

        self._max_severity_level = 0
        self._filename = None
        self._show_all = False

        if 'SHOW_ALL_VULNERABILITIES' in os.environ:
            self.show_all(True)

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

    def report(self):
        """
        Create a report of the non-tolerated vulnerabilities.

        Returns
        -------
        int
            Zero if all vulnerabilities have a tolerance less than or equal to
            the specified tolerance.  Non-zero otherwise.
        """
        tolerance_name = self.tolerance_name()
        valid_tolerance_names = self.valid_tolerance_names()

        if tolerance_name not in self.valid_tolerance_names():
            error_message = f'{tolerance_name} is not a valid tolerance '
            error_message += f'({",".join(valid_tolerance_names)})'
            raise ValueError(error_message)

        vulnerabilities = Vulnerabilities(self.show_all())
        unused_allowed_vulnerabilities = self.vulnerabilities_allowed_list()
        filename = self.filename()

        if filename:
            stream = open(filename)
            grype_data = json.load(stream)
            stream.close()
        else:
            grype_data = json.load(sys.stdin)

        logging.debug(
            f'Tolerance is {self.tolerance_name()} '
            + f'({self.tolerance_level()})'
        )
        logging.debug(f"Grype version {grype_data['descriptor']['version']}")

        if 'ONLY_FIXED' in os.environ and os.environ['ONLY_FIXED'] == '1':
            mesg = 'Only fixed vulnerabilities will be searched for.'
        else:
            mesg = 'All vulnerabilities (fixed or not) will be searched for.'

        logging.debug(mesg)

        for match in grype_data['matches']:
            matched_vulnerability = match['vulnerability']
            artifact = match['artifact']
            vulnerability_name = artifact['name']
            vulnerability_installed = artifact['version']
            vulnerability_id = matched_vulnerability['id']
            vulnerability_severity = matched_vulnerability['severity']
            level = self.tolerance_name2level(vulnerability_severity)

            if vulnerability_id in unused_allowed_vulnerabilities:
                unused_allowed_vulnerabilities.remove(vulnerability_id)

            if vulnerability_id in self.vulnerabilities_allowed_list():
                allowed = True
            else:
                allowed = False

            if level <= self.tolerance_level() and not self.show_all():
                add_vulnerability = False
            elif level <= self.tolerance_level() and self.show_all():
                add_vulnerability = True
            elif level > self.tolerance_level():
                if not allowed:
                    add_vulnerability = True
                    self.max_severity_level(level)
                elif allowed and self.show_all():
                    add_vulnerability = True
                else:
                    add_vulnerability = False

            if add_vulnerability:
                vulnerability = Vulnerability(vulnerability_id)
                vulnerability.name(vulnerability_name)
                vulnerability.installed_version(vulnerability_installed)
                vulnerability.severity(vulnerability_severity)
                vulnerability.allowed(allowed)
                vulnerabilities.add(vulnerability)

        print(vulnerabilities)

        if len(unused_allowed_vulnerabilities):
            for vulnerability_id in unused_allowed_vulnerabilities:
                if vulnerability_id.strip():
                    msg = f'"{vulnerability_id}" is in the allowed list '
                    msg += 'but not found in the scan!'
                    logging.warning(msg)

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
        """
        if tolerance_name is not None:
            self._tolerance_name = tolerance_name.capitalize()
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
