
Feature: Cart tests


  Scenario: User can verify cart is empty
    Given Open Target Main Page
    When Click on Cart icon
    Then Verify cart empty message is shown
    And Verify cart page opens