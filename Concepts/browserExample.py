# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# # Chrome Browser
# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# expected_title="Googles"
# actual_title=driver.title
# if expected_title == actual_title:
#     print("The title is equal to Googles")
# else:
#     print("The title is not equal to Googles")
# time.sleep(2)
# driver.quit()
# # Firefox Browser
# driver = webdriver.Firefox()
# driver.get("https://www.google.com")
# time.sleep(2)
# driver.quit()
# # Edge Browser
# driver = webdriver.Edge()
# driver.get("https://www.google.com")
# time.sleep(2)
# driver.quit()
#----------------------------------------------------------------
#Headless Mode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# Chrome Browser
myoptions = Options()
myoptions.add_argument("--headless")
# Start browser with correct syntax
driver = webdriver.Chrome(options=myoptions)
driver.get("https://www.google.com")
expected_title="Google"
actual_title=driver.title
if expected_title == actual_title:
    print("The title is correct")
else:
    print("The title is incorrect")
time.sleep(2)
driver.quit()