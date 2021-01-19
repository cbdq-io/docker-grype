# coding=utf-8
"""Allowed List feature tests."""
import os
import testinfra

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('../features/allowed_list.feature', 'No Allowed List')
def test_no_allowed_list():
    exception_message = 'VULNERABILITIES_ALLOWED_LIST is set in environment'
    assert 'VULNERABILITIES_ALLOWED_LIST' not in os.environ,\
        exception_message


@scenario('../features/allowed_list.feature', 'With allowed list')
def test_with_allowed_list():
    """With allowed list."""


@scenario('../features/allowed_list.feature',
          'With unnecessary vulnerability id in allowed list')
def test_with_unnecessary_vulnerability_id_in_allowed_list():
    """With unnecessary vulnerability id in allowed list."""


@given('test file is set', target_fixture='feature_data')
def test_file_is_set():
    """test file is set."""
    filename = 'tests/resources/grype.json'
    script = 'docker-grype/parse-grype-json.py'

    return {
        'command': f'{script} {filename}',
        'host_url': 'local://'
    }


@when('CVE-0000-42 in the allowed list')
def cve000042_in_the_allowed_list(feature_data):
    """CVE-0000-42 in the allowed list."""
    allowed_list = [
        'CVE-0000-42',
        'CVE-2018-12886',
        'CVE-2019-25013'
    ]
    os.environ['VULNERABILITIES_ALLOWED_LIST'] = ','.join(allowed_list)
    host = testinfra.get_host(feature_data['host_url'])
    cmd = host.run(feature_data['command'])
    feature_data['stderr'] = cmd.stderr
    feature_data['stdout'] = cmd.stdout


@when('CVE-2018-12886 in the allowed list')
def cve201812886_in_the_allowed_list(feature_data):
    """CVE-2018-12886 in the allowed list."""
    allowed_list = ['CVE-2018-12886', 'CVE-2019-25013']
    os.environ['VULNERABILITIES_ALLOWED_LIST'] = ','.join(allowed_list)
    host = testinfra.get_host(feature_data['host_url'])
    cmd = host.run(feature_data['command'])
    feature_data['stdout'] = cmd.stdout


@when('no allowed list provided')
def no_allowed_list_provided(feature_data):
    """no allowed list provided."""
    host = testinfra.get_host(feature_data['host_url'])
    cmd = host.run(feature_data['command'])
    feature_data['stdout'] = cmd.stdout


@then('expect CVE-0000-42 in stderr')
def expect_cve000042_in_stderr(feature_data):
    """expect CVE-0000-42 in stdout."""
    assert 'CVE-0000-42' in feature_data['stderr']


@then('expect CVE-2018-12886 in stdout')
def expect_cve201812886_in_stdout(feature_data):
    """expect CVE-2018-12886 in stdout."""
    assert 'CVE-2018-12886' in feature_data['stdout']


@then('expect no issues in stdout')
def expect_no_issues_in_stdout(feature_data):
    """expect no issues in stdout."""
    assert 'CVE' not in feature_data['stdout']
