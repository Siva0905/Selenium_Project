from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def locators_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://demo.opencart.com/")
        time.sleep(2)

        # 1. LINK_TEXT Locator - Click on "My Account"
        my_account = driver.find_element(By.LINK_TEXT, "My Account")
        my_account.click()
        time.sleep(2)

        # 2. PARTIAL_LINK_TEXT Locator - Click on "Login"
        login = driver.find_element(By.PARTIAL_LINK_TEXT, "Log")
        login.click()
        time.sleep(2)

        # 3. ID Locator - Enter email
        email = driver.find_element(By.ID, "input-email")
        email.send_keys("test@example.com")
        time.sleep(2)

        # 4. NAME Locator - Enter password
        password = driver.find_element(By.NAME, "password")
        password.send_keys("password123")
        time.sleep(2)

        # 5. CLASS_NAME Locator - Click login button
        login_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
        login_btn.click()
        time.sleep(2)

        # 6. TAG_NAME Locator - Count all input fields
        inputs = driver.find_elements(By.TAG_NAME, "input")
        print(f"Number of input fields: {len(inputs)}")
        time.sleep(2)

    finally:
        driver.quit()

locators_demo()
#------------------------------------------------------------------------------------
#Using CSS Selector
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def locators_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://demo.opencart.com/")
        time.sleep(2)

        # 1. CSS Selector: tag + class
        my_account = driver.find_element(By.CSS_SELECTOR, "a.dropdown-toggle")
        my_account.click()
        time.sleep(1)

        # 2. CSS Selector: tag + attribute
        login_link = driver.find_element(By.CSS_SELECTOR, "a[href*='route=account/login']")
        login_link.click()
        time.sleep(2)

        # 3. CSS Selector: tag + id
        email_input = driver.find_element(By.CSS_SELECTOR, "input#input-email")
        email_input.send_keys("test@example.com")
        time.sleep(1)

        # 4. CSS Selector: tag + name attribute
        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys("password123")
        time.sleep(1)

        # 5. CSS Selector: tag + class + attribute
        login_button = driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary[type='submit']")
        login_button.click()
        time.sleep(2)

        # 6. CSS Selector: tag only (counting all links)
        links = driver.find_elements(By.CSS_SELECTOR, "a")
        print(f"Number of links on the page: {len(links)}")

    finally:
        driver.quit()

locators_demo()