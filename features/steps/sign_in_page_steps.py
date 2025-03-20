from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify Sign-In form opened")
def verify_sign_in_form_opens(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsHeading']").text
    expected_text = "Sign into your Target account"
    assert expected_text in actual_text, f"Error. Text {expected_text} not found in {actual_text}"