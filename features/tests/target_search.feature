
Feature: Target Test Cases
#
  Scenario: User can search for a product on Target
    Given Open Target Main Page
    When Search for tea
    Then Verify correct search results show for tea
    And Verify tea in URL

#
#  Scenario: User can search for a product on Target
#    Given Open Target Main Page
#    When Search for coffee
#    Then Verify correct search results show for coffee


#  Scenario Outline: User can search for products on Target
#    Given Open Target Main Page
#    When search for <search_word>
#    Then Verify correct search results show for <product>
#    Examples:
#    |search_word  |product
#    |tea          |tea
#    |coffee       |coffee
#    |dress        |dress

  Scenario: Logged-out user can navigate to sign-in
    Given Open Target Main Page
    When Click on Sign-In
    And Click Sign-In from right navigation menu
    Then Verify Sign-In form opened

#
##
  Scenario: User can add any product into the cart
    Given Open Target Main Page
    When Search for plates
    And Click on add to cart button
    And Store product name
    And Click add to cart from side navigation window
    And Open Cart page
    Then Verify cart page opens
    And Verify cart has 1 item(s)
#    Then Verify cart has correct product