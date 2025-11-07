from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.wikipedia.org"
expected_title = "Wikipedia"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

actual_title = driver.title
if expected_title in actual_title:
    print("The title contains 'Wikipedia'")
else:
    print("The title does not contain 'Wikipedia'")

time.sleep(2)
driver.quit()
