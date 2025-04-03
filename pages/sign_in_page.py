from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[id='login']")
    EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "[id='username']")
    SIGN_IN_PAGE_TEXT = (By.CSS_SELECTOR, "[class*='styles_ndsHeading']")


    def enter_email_address(self):
        self.input_text("jraivitch@gmail.com")

    def click_continue_button(self):
        self.click(*self.CONTINUE_BUTTON)

    def verify_sign_in_page_opens(self):
        self.verify_text("Sign into your Target account", *self.EMAIL_ADDRESS_FIELD)

