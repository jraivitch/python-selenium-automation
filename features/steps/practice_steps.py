from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


LINKS  = (By.CSS_SELECTOR, "ul.navbar-nav li")
ELEMENT_TO_VERIFY_URL_LOADS = (By.CSS_SELECTOR, ".header-middle")
SIGN_IN_LOGIN_BUTTON = (By.LINK_TEXT, "Signup / Login")
NEW_USER_SIGNUP = (By.CSS_SELECTOR, "div[class='signup-form'] h2")
NAME_FIELD_SIGNUP = (By.NAME, "name")
EMAIL_FIELD_SIGNUP = (By.NAME, "email")
SIGN_UP_BUTTON = (By.CSS_SELECTOR, "[data-qa='signup-button']")


@given("Navigate to automation website")
def navigate_to_automation_website(context):
    context.driver.get("https://automationexercise.com/")
    context.driver.wait.until(EC.presence_of_element_located(ELEMENT_TO_VERIFY_URL_LOADS), message="Waiting for element to load")


@when("Verify home page is visible")
def verify_home_page_is_visible(context):
    context.driver.find_element(*ELEMENT_TO_VERIFY_URL_LOADS)


@when("Verify {link_number} links shown")
def verify_links_shown(context, link_number):
    links = context.driver.find_elements(*LINKS)
    link_number = int(link_number)
    assert link_number == len(links), f"Expected {link_number}, got {len(links)}"

@when("Click Sign-in/Login")
def click_sign_in(context):
    button = context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_LOGIN_BUTTON), message="Element not clickable")
    button.click()


@when("Verify 'New-User Signup' is visible")
def verify_new_user_signup(context):
    context.driver.wait.until(EC.visibility_of_element_located(NEW_USER_SIGNUP), message="Element not visible")
    context.driver.find_element(*NEW_USER_SIGNUP)


@when("Enter {name} and {email_address}")
def enter_name_and_email(context, name, email_address):
    context.name = name
    context.email_address = email_address
    context.driver.find_element(*NAME_FIELD_SIGNUP).send_keys(context.name)
    context.driver.find_element(*EMAIL_FIELD_SIGNUP).send_keys(context.email_address)


@when("Click Sign-up")
def click_signup(context):
    signup_button = context.driver.find_element(*SIGN_UP_BUTTON)
    signup_button.click()