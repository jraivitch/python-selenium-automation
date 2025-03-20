from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CELLS = (By.CSS_SELECTOR, "div[class*='cell-item-content']")


@given('Open Target Circle')
def open_target_circle(context):
    context.driver.get("https://www.target.com/circle")
    sleep(2)


@then("Verify at least 10 links  are shown")
def verify_benefit_cells_shown(context):
    links = context.driver.find_elements(*BENEFIT_CELLS)
    assert len(links) >= 10, f'{len(links)} links shown, expected >= 10'