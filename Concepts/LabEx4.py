from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Step 1: Scroll to bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
# Step 2: Scroll to top
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
# Step 3: Close browser
driver.quit()