# coding=utf-8
"""The Grype Container feature tests."""
import importlib
import os
import testinfra_bdd

from pytest_bdd import (
    scenarios,
    given,
    then,
    parsers
)

# Ensure that the PyTest fixtures provided in testinfra-bdd are available to
# your test suite.
pytest_plugins = testinfra_bdd.PYTEST_MODULES
scenarios('../features/grype.feature')
grype_parser = importlib.import_module('parse-grype-json')


@given(parsers.parse('VULNERABILITIES_ALLOWED_LIST="{allowed_list}"'), target_fixture='vulnerabilities_allowed_list')
def vulnerabilities_allowed_list(allowed_list):
    """VULNERABILITIES_ALLOWED_LIST="<allowed_list>"."""
    return allowed_list


@given('VULNERABILITIES_ALLOWED_LIST=""', target_fixture='vulnerabilities_allowed_list')
def vulnerabilities_allowed_list_is_blank():
    """VULNERABILITIES_ALLOWED_LIST="<allowed_list>"."""
    return ''


@given('the expected Grype version is set', target_fixture='expected_value')
def the_expected_grype_version_is_set():
    """the expected Grype version is set."""
    return os.environ['GRYPE_VERSION']


@then(parsers.parse('main return code is {expected_exit_code:d}'))
def the_command_return_code_is_expected_exit_code(expected_exit_code, vulnerabilities_allowed_list):
    """the command return code is <expected_exit_code>."""
    os.environ['VULNERABILITIES_ALLOWED_LIST'] = vulnerabilities_allowed_list
    assert grype_parser.main('tests/resources/grype.json') == expected_exit_code
