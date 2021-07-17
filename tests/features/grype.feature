Feature: Grype

  Scenario Outline: Grype Version
    Given the Grype container
    When the version is queried
    Then check the version matches <expected_version>

    Examples:
    | expected_version |
    | 0.15.0           |
