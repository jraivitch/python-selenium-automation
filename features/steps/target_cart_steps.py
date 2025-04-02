from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CART_DETAILS = (By.CSS_SELECTOR, "span[class='sc-93ec7147-3 htvqU']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@then("Verify cart empty message is shown")
def verify_empty_cart_message(context):
    context.app.cart_page.verify_empty_message_shown()

@then("Verify cart has {number_of_items} item(s)")
def verify_number_of_cart_items(context, number_of_items):
    context.app.cart_page.verify_items_in_cart(number_of_items)


@then("Verify cart has correct product")
def verify_cart_product(context):
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    assert context.product_name[:20] == product_name_in_cart[:20], f'Expected {context.product_name[:20]} but got {product_name_in_cart[:20]}'


@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()