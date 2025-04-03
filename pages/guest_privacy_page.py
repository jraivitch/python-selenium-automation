from pages.base_page import Page
from selenium.webdriver.common.by import By


class GuestPrivacyPage(Page):

    PRIVACY_POLICY_LINK = (By.CSS_SELECTOR, "[aria-label*='privacy']")

    def open_guest_pp_page(self):
        self.open_url("https://www.target.com/guest-privacy")

    def store_current_window(self):
        current_window = self.get_current_window_handle()
        print("Current window: ", current_window)

    def click_pp_link(self):
        self.wait_until_clickable_click(*self.PRIVACY_POLICY_LINK)

    def switch_to_guest_new_window(self):
        self.switch_to_new_window()

    def verify_PP_page_opened(self):
        self.verify_partial_url("target-privacy-policy")

    def close_and_switch_to_original_window(self):
        self.close()
