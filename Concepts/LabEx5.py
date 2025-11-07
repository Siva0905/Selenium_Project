from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Step 2: Take screenshot
driver.save_screenshot("practice_page.png")
# Step 3: Find "Broken Link"
broken_link = driver.find_element(By.LINK_TEXT, "Broken Link")
url = broken_link.get_attribute("href")
# Step 4: Check status code
response = requests.get(url, verify=False)
if response.status_code == 404:
    print("The link is broken!")
else:
    print("The link is valid.")
# Step 6: Close browser
driver.quit()