Feature: Allowed List
  Background: Test File
    Given test file is set

  Scenario: No Allowed List
    When no allowed list provided
    Then expect CVE-2018-12886 in stdout

  Scenario: With allowed list
    When CVE-2018-12886 in the allowed list
    Then expect no issues in stdout

  Scenario: With unnecessary vulnerability id in allowed list
    When CVE-0000-42 in the allowed list
    Then expect CVE-0000-42 in stderr
