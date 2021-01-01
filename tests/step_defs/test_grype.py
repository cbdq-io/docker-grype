# coding=utf-8
"""Grype feature tests."""
import testinfra

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('../features/grype.feature', 'Grype Version')
def test_grype_version():
    """Grype Version."""


@given('the Grype container', target_fixture='test_data')
def the_grype_container():
    """the Grype container."""
    test_data = {}
    test_data['host_url'] = "docker://grype"
    return test_data


@when('the version is queried')
def the_version_is_queried(test_data):
    """the version is queried."""
    host_url = test_data['host_url']
    host = testinfra.get_host(host_url)
    cmd = host.run("/usr/local/bin/grype version")
    assert cmd.succeeded, "Unable to query Grype version."
    lines = cmd.stdout.split('\n')
    grype_version = lines[1].split(':')[1].strip()
    test_data['grype_version'] = grype_version


@then('check the version matches <expected_version>')
def check_the_version_matches_expected_version(test_data, expected_version):
    """test the version matches <expected_version>."""
    grype_version = test_data['grype_version']
    error_message = f'Version {grype_version} != {expected_version}.'
    assert grype_version == expected_version, error_message
