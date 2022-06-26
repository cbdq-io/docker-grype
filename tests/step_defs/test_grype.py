# coding=utf-8
"""The Grype Container feature tests."""
import os

from pytest_bdd import (
    given,
    scenario,
    then
)

# Ensure that the PyTest fixtures provided in testinfra-bdd are available to
# your test suite.
pytest_plugins = ['testinfra_bdd']


@scenario('../features/grype.feature',
          'Assert the Container is Build as Expected')
def test_assert_the_container_is_build_as_expected():
    """Assert the Container is Build as Expected."""


@given('the expected version string', target_fixture='expected_version')
def the_expected_version_string():
    """the expected version string."""
    return os.environ['GRYPE_VERSION']


@then('check the version matches the expected version')
def check_the_version_matches_the_expected_version(testinfra_bdd_host,
                                                   expected_version):
    """check the version matches the expected version."""
    stream_name = 'stdout'
    stream = testinfra_bdd_host.get_stream_from_command(stream_name)
    message = f'The string "{expected_version}" was not found in the '
    message += f'{stream_name} ("{stream}") of the command.'
    assert expected_version in stream, message
