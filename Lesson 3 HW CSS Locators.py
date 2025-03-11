from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&prevRID=M9REZ6J1Q376YG2VSVR1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

sleep(5)

# CSS for amazon button on create account page
driver.find_element(By.CSS_SELECTOR, "a.a-link-nav-icon")

#CSS for Create Account Text
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

#CSS for Your Name box
driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

#CSS for Mobile Number or Email box
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#CSS for password box and re-enter password box
driver.find_element(By.CSS_SELECTOR, "#ap_password")
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

#CSS for Create Your Account button
driver.find_element(By.CSS_SELECTOR, "#continue")

#CSS for Conditions of Use Link
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use?']")

#CSS for Privacy Policy Link
driver.find_element(By.CSS_SELECTOR, "[href*='privacy_notice?']")

#CSS for Sign-in link
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')
