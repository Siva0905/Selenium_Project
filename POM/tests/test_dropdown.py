from selenium import webdriver
from selenium.webdriver.common.by import By
def test_dropdown_selection():
    driver=webdriver.Chrome()
    driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
    driver.switch_to.frame("iframeResult")
    dropdown = driver.find_element(By.NAME, "cars")
    options = dropdown.find_elements(By.TAG_NAME, "option")
    assert len(options) >= 6