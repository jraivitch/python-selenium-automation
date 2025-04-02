from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.CSS_SELECTOR, '#search')
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_RIGHT_NAV_BUTTON = (By.CSS_SELECTOR, "[class*='Content--after-open styles_ndsBaseModalDrawer']")


    def search(self, search_word):
        print("searching for {search_word}")
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

    def click_cart_icon(self, *locator):
        self.click(*self.CART_ICON)

    def click_sign_in(self, *locator):
        self.click(*self.SIGN_IN_BUTTON)

    def click_sign_in_right(self, *locator):
        self.click(*self.SIGN_IN_RIGHT_NAV_BUTTON)