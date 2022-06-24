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
        self._id_list = []
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

        for vulnerability in self._vulnerabilities:
            row = [
                vulnerability.name(),
                vulnerability.installed_version(),
                vulnerability.vulnerability_id,
                vulnerability.severity(),
                vulnerability.allowed()
            ]

            if not self._show_all:
                row = row[:-1]

            response += ','.join(row)
            response += '\n'

        return response

    def add(self, vulnerability):
        """
        Add a vulnerability to the list to be reported.

        Parameters
        ----------
        vulnerability : pygrype.vulnerability.Vulnerability
            The ID of the vulnerability (e.g. CVE-2011-3374).
        """
        # Avoid duplicated reporting on a single vulnerability.
        if vulnerability.vulnerability_id in self._id_list:
            return

        self._id_list.append(vulnerability.vulnerability_id)
        self._vulnerabilities.append(vulnerability)
