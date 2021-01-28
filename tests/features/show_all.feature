Feature: Show All

  Scenario Outline: Show All Scenarios
    Given the test file
    When the allowed list is <allowed_list>
    And show all is <show_all>
    Then status is <status>
    And the allowed column is <allowed_column_present>

    Examples:
    | allowed_list   | show_all | status | allowed_column_present |
    |                |          | 1      | False                  |
    |                | 1        | 1      | True                   |
    | CVE-2018-12886 |          | 0      | False                  |
    | CVE-2018-12886 | 1        | 0      | True                   |
