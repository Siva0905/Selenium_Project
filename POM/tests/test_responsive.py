from selenium import webdriver
from selenium.webdriver.common.by import By

def test_responsive_layout():
    driver = webdriver.Chrome()
    driver.set_window_size(375, 667)  # iPhone dimensions
    driver.get("https://www.saucedemo.com/")

    # Perform login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Now check for the responsive menu
    menu = driver.find_element(By.ID, "menu_button_container")
    assert menu.is_displayed()

    driver.quit()