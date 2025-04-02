from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg'] h1")
    CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")

    def verify_empty_message_shown(self):
        self.verify_text('Your cart is empty', *self.EMPTY_CART_MESSAGE)

    def open_cart_page(self, url):
        self.driver.get(url)

    def verify_items_in_cart(self, number_of_items):
        actual_number_of_items = self.find_element(*self.CART_ITEM_TITLE).text
        assert f'{number_of_items}' in actual_number_of_items, f'Expected {number_of_items} item(s) but got {actual_number_of_items} instead'

    def verify_cart_page_opens(self):
        self.verify_url('https://www.target.com/cart')


