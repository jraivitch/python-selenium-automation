from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given("Open Guest PP")
def open_page(context):
    context.app.guest_privacy_page.open_guest_pp_page()


@when("Store current guest window")
def store_guest_privacy_page(context):
    context.original_window = context.app.guest_privacy_page.store_current_window()


@when("Click on PP link")
def click_privacy_policy(context):
    context.app.guest_privacy_page.click_pp_link()


@when("Switch to PP link window")
def switch_to_guest_pp_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.app.guest_privacy_page.switch_to_guest_new_window()

@when("Verify PP window is open")
def verify_pp_window_is_open(context):
    context.app.guest_privacy_page.verify_PP_page_opened()

@then("User can close new window and switch back to original")
def user_close_new_window(context):
    context.app.guest_privacy_page.close_and_switch_to_original_window()
