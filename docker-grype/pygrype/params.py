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
    log_level : str
        Taken from the environment variable LOG_LEVEL.  Sets what the logging level should be
        (e.g. INFO).  Defaults to INFO.
    only_fixed : bool
        Taken from the ONLY_FIXED environment variable.  If set to '1' then only fixed bugs
        are to be reported.
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
        self.only_fixed = self.get_environment_value('ONLY_FIXED', '0') == '1'
        self.log_level = self.get_environment_value('LOG_LEVEL', 'INFO')
        self.show_all_vulnerabilities = self.get_environment_value('SHOW_ALL_VULNERABILITIES', '0') != '0'
        self.tolerance_name = self.get_environment_value('TOLERATE', 'Medium').capitalize()
        self.tolerance_level = severity_name_to_level(self.tolerance_name)

        vulnerabilities_allowed_list = []

        for vulnerability_id in self.get_environment_value('VULNERABILITIES_ALLOWED_LIST', '').split(','):
            vulnerability_id = vulnerability_id.strip()

            if vulnerability_id:
                vulnerabilities_allowed_list.append(vulnerability_id)

        self.vulnerabilities_allowed = vulnerabilities_allowed_list

    def get_environment_value(self, key_name, default_value):
        """
        Get an environment value or return a default string value if the key doesn't exist.

        Parameters
        ----------
        key_name : str
            The name of the environment variable.
        default_value : str
            The default value to set if the key name doesn't exist in the environment.

        Returns
        -------
        str
            Either the key value or the default.
        """
        if key_name in os.environ:
            return os.environ[key_name]
        return default_value
