from pages.base_page import Page
from selenium.webdriver.common.by import By

class TargetAppMainPage(Page):
    PP_LINK = (By.CSS_SELECTOR, "[aria-label='privacy policy - opens in a new window']")

    def open_target_app_page(self):
        self.open_url('https://www.target.com/c/target-app/-/N-4th2r')

    def click_pp_link(self):
        self.wait_until_clickable_click(*self.PP_LINK)

    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy')
