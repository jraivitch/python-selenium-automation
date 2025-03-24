from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")

    def verify_empty_message_shown(self):
        actual_text = self.find_element(*self.EMPTY_CART_MESSAGE).text
        expected_text = 'Your cart is empty'
        assert expected_text in actual_text, "Error. Text not found in {actual_text}"