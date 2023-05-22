"""
File: pygrype/params.py.

Extract the parameters from the environment variables.
"""
import os

from pygrype.vulnerabilities import severity_name_to_level


class Params:
    """
    A class that gathers data from the environment variables and sets them as attributes.

    Attributes
    ----------
    by_cve : bool
        Taken from the BY_CVE environment variable.  If set to '1' then
        orient results by CVE instead of the original vulnerability ID when
        possible.
    only_fixed : bool
        Taken from the ONLY_FIXED environment variable.  If set to '1' then only fixed bugs
        are to be reported.
    log_level : str
        Taken from the environment variable LOG_LEVEL.  Sets what the logging level should be
        (e.g. INFO).  Defaults to INFO.
    show_all_vulnerabilities : bool
        Taken from the SHOW_ALL_VULNERABILITIES environment variable.  If set to anything
        other than zero then set to True.
    tolerance_name : str
        Taken from the environment variable TOLERATE.  Sets what the maximum tolerance level
        will be (e.g. Medium or High).  Defaults to Medium.
    tolerance_level : int
        Set depending on the tolerance_name.
    vulnerabilities_allowed : list
        Taken from the VULNERABILITIES_ALLOWED_LIST environment variable.  The environment
        variable is a CSV list of vulnerability identifiers that are tolerated in the
        scan.
    """

    def __init__(self):
        """Construct a Params object."""
        self.by_cve = os.environ.get('BY_CVE', '0') == '1'
        self.only_fixed = os.environ.get('ONLY_FIXED', '0') == '1'
        self.log_level = os.environ.get('LOG_LEVEL', 'INFO')
        self.show_all_vulnerabilities = os.environ.get('SHOW_ALL_VULNERABILITIES', '0') != '0'
        self.tolerance_name = os.environ.get('TOLERATE', 'Medium').capitalize()
        self.tolerance_level = severity_name_to_level(self.tolerance_name)

        vulnerabilities_allowed_list = []

        for vulnerability_id in os.environ.get('VULNERABILITIES_ALLOWED_LIST', '').split(','):
            vulnerability_id = vulnerability_id.strip()

            if vulnerability_id:
                vulnerabilities_allowed_list.append(vulnerability_id)

        self.vulnerabilities_allowed = vulnerabilities_allowed_list
