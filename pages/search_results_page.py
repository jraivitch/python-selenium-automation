from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    SIDE_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")

    def verify_search_results(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def click_add_to_cart_button(self, *locator):
        self.find_element(*self.ADD_TO_CART_BUTTON).click()

    def store_product_name(self, *locator):
        product_name = self.find_element(*self.SIDE_NAV_PRODUCT_NAME).text

    def side_nav_add_to_cart_button(self, *locator):
        self.click(*self.SIDE_ADD_TO_CART_BUTTON)

    def verify_partial(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url)