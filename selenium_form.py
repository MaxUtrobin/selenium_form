# Open https://the-internet.herokuapp.com/login
# Please automate next test cases:
# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
# 2. Login with invalid creds and check validation error
# 3. Logout from app and assert you successfully logged out
# ----------------------------------------------------------------------------------------------------------
import time
from selenium import webdriver
# ----------------------------------------------------------------------------------------------------------
# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
# ----------------------------------------------------------------------------------------------------------
TEST_DATA = {
        'username': 'tomsmith',
        'password': 'SuperSecretPassword!',
    }
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)
driver.find_element_by_css_selector("#username").send_keys(TEST_DATA['username'])
driver.find_element_by_css_selector("#password").send_keys(TEST_DATA['password'])
driver.find_element_by_css_selector("#login > button > i").click()
elem = driver.find_element_by_css_selector('[id="flash"]').text
assert 'You logged into a secure area!' in elem
time.sleep(2)
driver.quit()
# ----------------------------------------------------------------------------------------------------------
# 2. Login with invalid creds and check validation error
# ----------------------------------------------------------------------------------------------------------
TEST_DATA = {
        'username': '123123123',
        'password': '123123132',
    }
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)
driver.find_element_by_css_selector("#username").send_keys(TEST_DATA['username'])
driver.find_element_by_css_selector("#password").send_keys(TEST_DATA['password'])
driver.find_element_by_css_selector("#login > button > i").click()
elem = driver.find_element_by_css_selector('[id="flash"]').text
assert 'Your username is invalid!' in elem
time.sleep(2)
driver.quit()
# ----------------------------------------------------------------------------------------------------------
# 3. Logout from app and assert you successfully logged out
# ----------------------------------------------------------------------------------------------------------
TEST_DATA = {
        'username': 'tomsmith',
        'password': 'SuperSecretPassword!',
    }
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)
driver.find_element_by_css_selector("#username").send_keys(TEST_DATA['username'])
driver.find_element_by_css_selector("#password").send_keys(TEST_DATA['password'])
driver.find_element_by_css_selector("#login > button > i").click()
time.sleep(2)
driver.find_element_by_css_selector("#content > div > a > i").click()
time.sleep(2)
elem = driver.find_element_by_css_selector('[id="flash"]').text
assert 'You logged out of the secure area!' in elem
time.sleep(2)
driver.quit()