from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGN_IN = (By.CSS_SELECTOR, "#account-sign-in")
NAV_BAR_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")



@given("Open Target Main")
def open_target_main_page(context):
    context.driver.get('https://www.target.com')
    sleep(5)


@when("Click Sign-In")
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN).click()
    sleep(5)


@when("Click Sign-in from side navigation bar")
def click_sign_in_from_side_navigation(context):
    context.driver.find_element(*NAV_BAR_SIGN_IN).click()
    sleep(5)


@then("Verify Sign-in form opened")
def verify_sign_in_form_opened(context):
    context.driver.find_element(By.CSS_SELECTOR, "[id='login']")
    sleep(3)
    print("Sign-in form opened")