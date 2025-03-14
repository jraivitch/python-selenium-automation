# Created by jraiv at 3/14/2025
Feature: Target Circle Page
  # Enter feature description here

  Scenario: User can open the Target Circle Page
    Given Open Target Circle Page
    Then Verify links are present


  Scenario: User can search for a product on Target Circle
    Given Open Target Circle Page
    When Search for coffee
    Then Verify coffee is shown as a result


  Scenario: User can search for a product on Target Circle
    Given Open Target Circle Page
    When Search for tea
    Then Verify tea is shown as a result


