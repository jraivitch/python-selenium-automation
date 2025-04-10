from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.Target_App_Main_page import TargetAppMainPage
from pages.guest_privacy_page import GuestPrivacyPage

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.Target_App_Main_page = TargetAppMainPage(driver)
        self.guest_privacy_page = GuestPrivacyPage(driver)