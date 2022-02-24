# coding=utf-8
"""Grype feature tests."""
import os
import pytest
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
    try:
        expected_version = os.environ['GRYPE_VERSION']
        test_data = {
            'expected_version': expected_version,
            'host_url': "docker://grype"
        }
    except KeyError:
        pytest.skip('GRYPE_VERSION not set in environment.')

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


@then('check the version matches the expected version')
def check_the_version_matches_expected_version(test_data):
    """test the version matches <expected_version>."""
    actual_version = test_data['grype_version']
    error_message = f'Version {actual_version} != {expected_version}.'
    assert grype_version == expected_version, error_message
