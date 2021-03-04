Feature: Show All

  Scenario Outline: Show All Scenarios
    Given the test file
    When the allowed list is <allowed_list>
    And show all is <show_all>
    Then status is <status>
    And the allowed column is <allowed_column_present>
    And column count matches <column_count>

    Examples:
    | allowed_list   | show_all | status | allowed_column_present | column_count |
    |                |          | 1      | False                  | 4            |
    |                | 1        | 1      | True                   | 5            |
    | CVE-2018-12886 |          | 0      | False                  | 4            |
    | CVE-2018-12886 | 1        | 0      | True                   | 5            |
