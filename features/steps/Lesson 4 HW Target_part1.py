from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")


@given("Open Target Main Page")
def open_target_main_page(context):
    context.driver.get('https://www.target.com')
    sleep(5)


@when("Click on Cart Icon")
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)


@then("Verify Cart is empty")
def verify_cart_is_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

