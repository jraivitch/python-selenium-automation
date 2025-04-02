
class Page:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)


    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert actual_text == expected_text, f"{actual_text} != {expected_text}"

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f"{expected_text} not in {actual_text}"

    def verify_partial_url(self, expected_partial_url):
        current_url = self.driver.current_url
        assert expected_partial_url in current_url, f"{expected_partial_url} not in {current_url}"


    def verify_url(self, expected_url):
        current_url = self.driver.current_url
        assert expected_url == current_url, f"{expected_url} != {current_url}"