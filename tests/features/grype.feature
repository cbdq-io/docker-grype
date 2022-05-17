Feature: The Grype Container

  Scenario: Assert the Container is Build as Expected
    Given the host with URL "docker://grype" is ready within 15 seconds
    And the expected version string
    When the command is "/usr/local/bin/grype version"
    Then the command return code is 0
    And check the version matches the expected version
    And the command stderr is empty
