from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Index.html")
# Step 2: Click "Skip Sign In"
driver.find_element(By.ID, "btn2").click()
# Step 3: Enter First Name using placeholder
driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Siva")
# Step 4: Enter Last Name using ng-model
driver.find_element(By.XPATH, "//input[@ng-model='LastName']").send_keys("Prakasam")
# ✅ Step 5: Enter Address using ng-model instead of rows/cols
driver.find_element(By.XPATH, "//textarea[@ng-model='Adress']").send_keys("123, Sample Street, Chennai")
# Step 6: Get header text
header_text = driver.find_element(By.TAG_NAME, "h1").text
print("Header Text:", header_text)
# Step 8: Navigate back
driver.back()
# Step 9: Close browser
driver.quit()