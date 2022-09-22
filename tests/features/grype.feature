Feature: The Grype Container

  Scenario: Assert the Container is Built as Expected
    Given the host with URL "docker://grype" is ready
    When the command is "/usr/local/bin/grype version"
    Then the command return code is 0
    And the command stdout contains "0.50.2"
    And the command stderr is empty

  Scenario Outline: Test Script Output and Exit Code
    Given the host with URL "docker://grype" is ready
    When the command is "SHOW_ALL_VULNERABILITIES=<show_all> VULNERABILITIES_ALLOWED_LIST=<allowed_list> /usr/local/bin/parse-grype-json.py /tmp/grype.json"
    Then the command return code is <expected_exit_code>
    And the command <stream_name> contains "<expected_string>"
    Examples:
      | allowed_list              | show_all | expected_exit_code | stream_name | expected_string                                                |
      |                           | 0        | 5                  | stdout      | CVE-2018-12886,Critical                                        |
      |                           | 1        | 5                  | stdout      | CVE-2018-12886,Critical,no                                     |
      | CVE-2018-12886            | 1        | 0                  | stdout      | CVE-2018-12886,Critical,yes                                    |
      | CVE-0000-0,CVE-2018-12886 | 0        | 0                  | stderr      | "CVE-0000-0" is in the allowed list but not found in the scan! |
      | CVE-0000-0,CVE-2018-12886 | 1        | 0                  | stderr      | "CVE-0000-0" is in the allowed list but not found in the scan! |
