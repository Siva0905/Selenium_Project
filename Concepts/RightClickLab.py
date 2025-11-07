from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def right_click_demo_webdriveruniversity():
    driver = webdriver.Chrome()
    try:
        driver.get("http://webdriveruniversity.com/Actions/index.html")
        actions = ActionChains(driver)

        # Locate the right-click box
        right_click_box = driver.find_element(By.ID, "double-click")

        # Perform right-click
        actions.context_click(right_click_box).perform()
        time.sleep(2)

        # No direct message appears, but you can verify the context menu or use JS alerts if needed
        print("Right-click performed on the box.")

    finally:
        driver.quit()

right_click_demo_webdriveruniversity()
