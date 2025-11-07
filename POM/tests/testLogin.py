# tests/test_login_and_profile.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# tests/test_login_ui.py

@pytest.mark.parametrize("driver", ["chrome"], indirect=True)
def test_login_functionality(driver):
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    # locate username, password fields and login button
    driver.find_element("id", "username").send_keys("tomsmith")
    driver.find_element("id", "password").send_keys("SuperSecretPassword!")
    driver.find_element("css selector", "button.radius").click()

    # verify successful login message
    success_msg = driver.find_element("css selector", "div.flash.success").text
    assert "You logged into a secure area!" in success_msg

