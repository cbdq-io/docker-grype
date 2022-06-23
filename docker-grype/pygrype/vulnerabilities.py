"""File: pygrype/vulnerabilities.py."""


class Vulnerabilities:
    """Collate and report on vulnerabilities."""

    def __init__(self, show_all):
        """
        Create a Vulnerabilities class.

        Parameters
        ----------
        show_all : bool
            Are all vulnerabilities (not just failing ones) be shown.
        """
        self._vulnerabilities = []
        self._show_all = show_all

    def __str__(self):
        """
        Return the vulnerability details as a CSV.

        Returns
        -------
        str
            A CSV string (with header).
        """
        if self._show_all:
            response = 'NAME,INSTALLED,VULNERABILITY,SEVERITY,ALLOWED\n'
        else:
            response = 'NAME,INSTALLED,VULNERABILITY,SEVERITY\n'

        for row in self._vulnerabilities:
            if not self._show_all:
                row = row[:-1]

            response += ','.join(row)
            response += '\n'

        return response

    def add(self, name, installed, vulnerability, severity, allowed):
        """
        Add a vulnerability to the list.

        Parameters
        ----------
        name : str
            The name of the vulnerability (e.g. apt).
        installed : str
            The version of the installed software (e.g. 1.8.2.2).
        vulnerability : str
            The ID of the vulnerability (e.g. CVE-2011-3374).
        severity : str
            The severity of the vulnerability.
        allowed : bool
            Is the vulnerability in the allowed list.
        """
        if allowed:
            allowed = 'yes'
        else:
            allowed = 'no'

        for v in self._vulnerabilities:
            if v[2] == vulnerability:
                return

        self._vulnerabilities.append([
            name,
            installed,
            vulnerability,
            severity,
            allowed])
