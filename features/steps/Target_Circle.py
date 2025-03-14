from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_BAR = (By.ID, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
LINKS_TARGET_CIRCLE = (By.CSS_SELECTOR, ".cell-item-content")

@given("Open Target Circle Page")
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9')
    sleep(3)


@when("Search for {product}")
def search_for_product(context, product):
    context.driver.find_element(*SEARCH_BAR).send_keys(product)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(3)


@then("Verify {product} is shown as a result")
def verify_product_result(context, product):
    context.driver.find_element(By.CSS_SELECTOR, "[class='h-text-bs h-display-flex h-flex-align-center h-text-grayDark h-margin-l-x2']")


@then('Verify Links are shown')
def verify_links_shown(context):
    context.driver.find_element(*LINKS_TARGET_CIRCLE)



