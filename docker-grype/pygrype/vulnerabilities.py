"""File: pygrype/vulnerabilities.py."""


def severity_level_to_name(severity_level):
    """
    Convert a severity level to a name.

    Parameters
    ----------
    severity_level : int
        The severity level as an integer.

    Returns
    -------
    str
        The severity level as a name.

    Raises
    ------
    ValueError
        If the provided level is not recognised.
    """
    severity_map = {
        0: 'Unknown',
        1: 'Negligible',
        2: 'Low',
        3: 'Medium',
        4: 'High',
        5: 'Critical'
    }

    if severity_level not in severity_map:
        raise ValueError(f'{severity_level} is not a recognised severity level.')
    return severity_map[severity_level]


def severity_name_to_level(severity_name):
    """
    Convert a name to a level.

    Parameters
    ----------
    severity_name : str
        The severity name.

    Returns
    -------
    int
        The corresponding integer level of the name.

    Raises
    ------
    ValueError
        If the provided name is not recognised.
    """
    severity_map = {
        'Unknown': 0,
        'Negligible': 1,
        'Low': 2,
        'Medium': 3,
        'High': 4,
        'Critical': 5
    }

    if severity_name not in severity_map:
        raise ValueError(f'{severity_name} is not a recognised severity name.')
    return severity_map[severity_name]


class Vulnerabilities:
    """Collate and report on vulnerabilities."""

    def __init__(self, params):
        """
        Create a Vulnerabilities class.

        Parameters
        ----------
        params : pgrype.params.Params
            The runtime parameters.
        """
        self.vulnerabilities = []
        self._id_list = []
        self.params = params

    def __str__(self):
        """
        Return the vulnerability details as a CSV.

        Returns
        -------
        str
            A CSV string (with header).
        """
        if self.params.show_all_vulnerabilities:
            response = 'NAME,INSTALLED,VULNERABILITY,SEVERITY,ALLOWED\n'
        else:
            response = 'NAME,INSTALLED,VULNERABILITY,SEVERITY\n'

        for vulnerability in self.vulnerabilities:
            row = [
                vulnerability.name(),
                vulnerability.installed_version(),
                vulnerability.vulnerability_id,
                vulnerability.severity(),
                vulnerability.allowed()
            ]

            if not self.params.show_all_vulnerabilities:
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
        self.vulnerabilities.append(vulnerability)

    def missing_and_allowed(self):
        """
        Provide a list of vulnerabilitiy ids that are in the allowed list, but not found in the scan.

        Returns
        -------
        list
            The list of allowed identifiers that are not in the scan.
        """
        response = self.params.vulnerabilities_allowed

        for vulnerability in self.vulnerabilities:
            vid = vulnerability.vulnerability_id

            if vid in response:
                response.remove(vid)

        return response
