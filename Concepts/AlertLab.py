from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def alerts_demo_automationtesting():
    driver = webdriver.Chrome()
    try:
        driver.get("https://demo.automationtesting.in/Alerts.html")
        # 1. Simple Alert
        driver.find_element(By.XPATH, "//button[@onclick='alertbox()']").click()
        time.sleep(1)
        alert = driver.switch_to.alert
        print(f"Simple Alert Text: {alert.text}")
        alert.accept()
        print("Simple alert accepted")
        time.sleep(1)
        # 2. Confirmation Alert
        driver.find_element(By.LINK_TEXT, "Alert with OK & Cancel").click()
        driver.find_element(By.XPATH, "//button[@onclick='confirmbox()']").click()
        time.sleep(1)
        alert = driver.switch_to.alert
        print(f"Confirmation Alert Text: {alert.text}")
        alert.dismiss()
        print("Confirmation alert dismissed")
        time.sleep(1)
        # 3. Prompt Alert
        driver.find_element(By.LINK_TEXT, "Alert with Textbox").click()
        driver.find_element(By.XPATH, "//button[@onclick='promptbox()']").click()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.send_keys("Selenium Python")
        print("Text entered in prompt")
        alert.accept()
        print("Prompt alert accepted")
    finally:
        driver.quit()
alerts_demo_automationtesting()