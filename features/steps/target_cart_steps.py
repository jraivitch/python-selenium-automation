from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_DETAILS = (By.CSS_SELECTOR, "span[class='sc-93ec7147-3 htvqU']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then("Verify cart empty message is shown")
def verify_empty_cart_message(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f"Error. Text {expected_text} not found in {actual_text}"


@then("Verify cart has {number_of_items} item(s)")
def verify_number_of_cart_items(context, number_of_items):
    actual_number_of_items = context.driver.find_element(*CART_DETAILS).text
    assert f'{number_of_items}' in actual_number_of_items, f'Expected {number_of_items} item(s) but got {actual_number_of_items} instead'


@then("Verify cart has correct product")
def verify_cart_product(context):
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name[:20] == product_name_in_cart[:20], f'Expected {context.product_name[:20]} but got {product_name_in_cart[:20]}'
