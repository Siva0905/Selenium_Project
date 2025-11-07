from selenium import webdriver
from selenium.webdriver.common.by import By
import time
url = "https://www.wikipedia.org"
expected_title = "Wikipedia"

# Chrome Browser
driver = webdriver.Chrome()
driver.get(url)
actual_title = driver.title
if expected_title in actual_title:
    print("Chrome: The title contains 'Wikipedia'")
else:
    print("Chrome: The title does not contain 'Wikipedia'")
time.sleep(2)
driver.quit()


