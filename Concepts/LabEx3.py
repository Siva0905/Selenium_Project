from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
# Step 2: Select "Skills"
skills_dropdown = Select(driver.find_element(By.ID, "Skills"))
skills_dropdown.select_by_visible_text("Adobe Photoshop")
# Step 3: Select "Country"
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_value("India")
# Step 4: Close browser
driver.quit()