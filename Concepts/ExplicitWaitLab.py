from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def explicit_wait_demo_practice_test():
    driver = webdriver.Chrome()
    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Wait for username field
        wait = WebDriverWait(driver, 10)
        username = wait.until(EC.presence_of_element_located((By.ID, "username")))
        username.send_keys("student")
        password = driver.find_element(By.ID, "password")
        password.send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        # Wait for success message
        success_message = wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        )
        print("Login successful:", success_message.text)
        # Wait for logout button
        logout_btn = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Log out"))
        )
        logout_btn.click()
        print("Logged out successfully")
    finally:
        driver.quit()
explicit_wait_demo_practice_test()
