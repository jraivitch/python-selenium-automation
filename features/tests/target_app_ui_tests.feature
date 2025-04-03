# Created by jraiv at 4/3/2025
Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy Page
    Given Open Target App Page
    And Store original window
    When Click on Privacy Policy
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window


