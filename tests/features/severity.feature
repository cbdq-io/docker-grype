Feature: Vulnerability Severity

    Scenario Outline: Verify the Correct Severity for a Vulnerability is Identified
        Given the vulnerability <vulnerability>
        Then the severity is <severity>
        Examples:
            | vulnerability       | severity |
            | GHSA-5cpq-8wj7-hf2v | Low      |
            | CVE-2023-34395      | Medium   |
