Feature: Grype

  Scenario Outline: Grype Version
    Given the Grype container
    When the version is queried
    Then check the version matches the expected version
