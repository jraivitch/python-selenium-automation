# Created by jraiv at 4/3/2025
Feature: verify that a user can open privacy policy from guest privacy page

  Scenario: User can open and close privacy policy page
    Given Open Guest PP
    When Store current guest window
    And Click on PP link
    And Switch to PP link window
    And Verify PP window is open
    Then User can close new window and switch back to original
#
