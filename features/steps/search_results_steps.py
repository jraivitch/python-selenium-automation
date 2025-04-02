from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@then("Verify correct search results show for {product}")
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)

@then('Verify {expected_text} in URL')
def verify_partial_url(context, expected_text):
    context.app.search_results_page.verify_partial(expected_text)