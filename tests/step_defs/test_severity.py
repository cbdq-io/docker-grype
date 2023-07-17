"""Vulnerability Severity feature tests."""
import json

from pytest_bdd import (
    given,
    parsers,
    scenario,
    then
)

from pygrype.params import Params
from pygrype.parser import ParseGrypeJSON


@scenario('../features/severity.feature', 'Verify the Correct Severity for a Vulnerability is Identified')
def test_verify_the_correct_severity_for_a_vulnerability_is_identified():
    """Verify the Correct Severity for a Vulnerability is Identified."""


@given(parsers.parse('the vulnerability {vulnerability}'), target_fixture='widget')
def _(vulnerability: str):
    """the vulnerability <vulnerability>."""
    with open(f'tests/resources/{vulnerability}.json') as stream:
        data = json.load(stream)
        vulnerability_match = data['matches'][0]

    return {
        'artifact': vulnerability_match['artifact'],
        'matched_vulnerability': vulnerability_match['vulnerability'],
        'related_vulnerabilities': vulnerability_match['relatedVulnerabilities']
    }


@then(parsers.parse('the severity is {severity}'))
def _(severity: str, widget: dict):
    """the severity is <severity>."""
    artifact = widget['artifact']
    matched_vulnerability = widget['matched_vulnerability']
    related_vulnerabilities = widget['related_vulnerabilities']

    params = Params()
    params.tolerance_name = 'Negligible'
    params.tolerance_level = 0

    parser = ParseGrypeJSON(params)
    vulnerability = parser.analyse_a_vulnerability(artifact, matched_vulnerability, related_vulnerabilities)
    assert vulnerability.severity() == severity
