# Created by jraiv at 3/11/2025
Feature: Lesson 3 HW Target Search
  # Enter feature description here

  Scenario: User can verify cart is empty
    Given Open Target Main Page
    When  Click on Cart Icon
    Then Verify Cart is empty
