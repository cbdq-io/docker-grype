# coding=utf-8
"""Show All feature tests."""
import os
import testinfra

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('../features/show_all.feature', 'Show All Scenarios')
def test_show_all_scenarios():
    """Show All Scenarios."""


@given('the test file', target_fixture='feature_data')
def the_test_file():
    """the test file."""
    filename = 'tests/resources/grype.json'
    script = 'docker-grype/parse-grype-json.py'

    return {
        'command': f'{script} {filename}',
        'host_url': 'local://'
    }


@when('show all is <show_all>')
def show_all_is_show_all(feature_data, show_all):
    """show all is <show_all>."""
    if show_all.strip() == '':
        if 'SHOW_ALL_VULNERABILITIES' in os.environ:
            os.environ.pop('SHOW_ALL_VULNERABILITIES')
    else:
        os.environ['SHOW_ALL_VULNERABILITIES'] = show_all.strip()


@when('the allowed list is <allowed_list>')
def the_allowed_list_is_allowed_list(feature_data, allowed_list):
    """the allowed list is <allowed_list>."""
    os.environ['VULNERABILITIES_ALLOWED_LIST'] = allowed_list.strip()


@then('column count matches <column_count>')
def column_count_matches_column_count(feature_data, column_count):
    """column count matches <column_count>."""
    expected_column_count = int(column_count)
    lines = []

    for line in feature_data['stdout'].split('\n'):
        line = line.strip()

        if line != '':
            lines.append(line)

    for line in lines:
        actual_column_count = len(line.split(','))
        message = f'Expected {expected_column_count} columns in '
        message += f'"{line}" but found {actual_column_count}.'
    assert actual_column_count == expected_column_count, message


@then('status is <status>')
def status_is_status(feature_data, status):
    """status is <status>."""
    host_url = feature_data['host_url']
    host = testinfra.get_host(host_url)
    cmd = host.run(feature_data['command'])
    feature_data['stdout'] = cmd.stdout

    if status.strip() == '0':
        assert cmd.succeeded, "Command returned error."
    else:
        assert not cmd.succeeded, "Command unexpectedly succeeded."


@then('the allowed column is <allowed_column_present>')
def the_allowed_column_is_allowed_column_present(feature_data,
                                                 allowed_column_present):
    """the allowed column is <allowed_column_present>."""
    expect_allowed_column = allowed_column_present == 'True'
    is_present = ',ALLOWED' in feature_data['stdout']
    assert expect_allowed_column == is_present
