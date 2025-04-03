from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

@given("Open Target App Page")
def open_target_app_page(context):
    context.app.Target_App_Main_page.open_target_app_page()


@given("Store original window")
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window: ', context.original_window)


@when("Click on Privacy Policy")
def click_privacy_policy(context):
    context.app.Target_App_Main_page.click_pp_link()


@when("Switch to new window")
def switch_to_window(context):
    context.app.base_page.switch_to_new_window()


@then("Verify Privacy Policy page opened")
def verify_privacy_policy_page_opened(context):
    context.app.Target_App_Main_page.verify_pp_opened()


@then('Close current page')
def close_current_page(context):
    context.app.base_page.close()


@then("Return to original window")
def return_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)
