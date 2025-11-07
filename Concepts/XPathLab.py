from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def xpath_examples_demo_site():
    driver = webdriver.Chrome()

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        # Username field
        username = driver.find_element(By.XPATH, "//input[@id='username']")
        username.send_keys("tomsmith")

        # Password field
        password = driver.find_element(By.XPATH, "//input[@id='password']")
        password.send_keys("SuperSecretPassword!")

        # Corrected XPath for login button
        login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_btn.click()

        time.sleep(3)

        # Logout button after login
        logout_btn = driver.find_element(By.XPATH, "//a[@href='/logout']")
        print("Logout button found:", logout_btn.is_displayed())

    finally:
        driver.quit()

xpath_examples_demo_site()