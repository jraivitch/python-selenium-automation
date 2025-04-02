from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):

    SIGN_IN_PAGE_TEXT = (By.CSS_SELECTOR, "[class*='styles_ndsHeading']")

    def verify_sign_in_page_opens(self):
        self.verify_text("Sign into your Target account", *self.SIGN_IN_PAGE_TEXT)
