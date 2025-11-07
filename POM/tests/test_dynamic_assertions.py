from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By



def test_loading_spinner():
    driver = webdriver.Chrome()
    driver.get("https://demo.seleniumeasy.com/dynamic-data-loading-demo.html")
    driver.find_element(By.ID, "save").click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "loading"))
    )