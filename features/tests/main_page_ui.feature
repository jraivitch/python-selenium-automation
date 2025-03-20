
Feature: Main page UI tests
  # Enter feature description here

  Scenario: Verify header links has at least 1 link
    Given Open Target Main Page
    Then Verify at least 1 link shown

  Scenario: Verify all header links shown
    Given Open Target Main Page
    Then Verify 6 links shown