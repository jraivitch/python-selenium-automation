# Created by jraiv at 3/11/2025
Feature: Lesson 3 HW Target Search Part 2
  # Enter feature description here

  Scenario: Logged out user can navigate to sign-in
    Given Open Target Main
    When  Click Sign-In
    And Click Sign-in from side navigation bar
    Then Verify Sign-in form opened