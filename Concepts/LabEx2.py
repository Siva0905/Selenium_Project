from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
# Step 2: Select "Male" radio button
male_radio = driver.find_element(By.XPATH, "//input[@value='Male']")
male_radio.click()
# Step 3: Check if selected
print("Male selected:", male_radio.is_selected())
# Step 4: Select "Cricket" checkbox
cricket_checkbox = driver.find_element(By.XPATH, "//input[@value='Cricket']")
cricket_checkbox.click()
# Step 5: Select "Movies" checkbox
movies_checkbox = driver.find_element(By.XPATH, "//input[@value='Movies']")
movies_checkbox.click()
# Step 6: Deselect "Movies"
movies_checkbox.click()
# Step 7: Verify status
print("Cricket selected:", cricket_checkbox.is_selected())
print("Movies selected:", movies_checkbox.is_selected())
# Step 8: Close browser
driver.quit()