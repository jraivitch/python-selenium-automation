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
driver.get('https://www.target.com/')

#Click Sign-in button
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(5)
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(5)

#verification
driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']")
print('Test Passed')