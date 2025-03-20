from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@then("Verify correct search results show for {product}")
def verify_search_results(context, product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert product in actual_text, f"Error. Text {product} not found in {actual_text}."