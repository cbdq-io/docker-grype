# coding=utf-8
"""The Grype Container feature tests."""

import testinfra_bdd

from pytest_bdd import scenario

# Ensure that the PyTest fixtures provided in testinfra-bdd are available to
# your test suite.
pytest_plugins = testinfra_bdd.PYTEST_MODULES


@scenario('../features/grype.feature',
          'Assert the Container is Built as Expected')
def test_assert_the_container_is_built_as_expected():
    """Assert the Container is Build as Expected."""


@scenario('../features/grype.feature', 'Test Script Output and Exit Code')
def test_test_script_output_and_exit_code():
    """Test Script Output and Exit Code."""
