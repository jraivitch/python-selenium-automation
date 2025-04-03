from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.CSS_SELECTOR, '#search')
SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
PRODUCT_SEARCH_RESULT_COUNT = (By.CSS_SELECTOR, "[data-test='lp-resultsCount']")



@given("Open Target Main Page")
def open_target_main_page(context):
    context.app.main_page.open_main_page()

@when("Search for {search_word}")
def search_product(context, search_word):
    context.app.header.search(search_word)
    context.driver.wait.until(EC.element_to_be_clickable(SEARCH_BUTTON)).click()



@when("Click on Cart Icon")
def click_cart_icon(context):
    context.app.header.click_cart_icon(CART_ICON)


@when("Click on Sign-In")
def click_sign_in(context):
    context.app.header.click_sign_in()



@when("Click Sign-In from right navigation menu")
def right_navigation_menu_sign_in(context):
   context.app.header.click_sign_in_right()


@when("Click on add to cart button")
def add_to_cart(context):
    context.driver.wait.until(EC.visibility_of_element_located(PRODUCT_SEARCH_RESULT_COUNT), message="Product not found")
    context.app.search_results_page.click_add_to_cart_button()



@when("Store product name")
def store_product_name(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))
    context.app.search_results_page.store_product_name(SIDE_NAV_PRODUCT_NAME)


@when("Click add to cart from side navigation window")
def add_to_cart_from_side(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message="Add to cart from side navigation window not found"
    )
    context.app.search_results_page.side_nav_add_to_cart_button(SIDE_ADD_TO_CART_BUTTON)




@when("Open Cart page")
def open_cart_page(context):
    context.app.cart_page.open_cart_page('https://www.target.com/cart')


@then("Verify at least 1 link shown")
def verify_1_header_link(context):
    link = context.driver.find_elements(*HEADER_LINKS)
    print(link)


@then("Verify {link_amount} links shown")
def verify_all_header_links(context, link_amount):
    links = context.driver.find_elements(*HEADER_LINKS)
    link_amount = int(link_amount)
    assert len(links) == link_amount, f'Expected {link_amount} links, found {len(links)}'
    print(links)


@then("Verify {product} was added into cart")
def  verify_product_added(context, product):
    context.driver.find_element()

