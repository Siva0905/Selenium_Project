from selenium import webdriver
from selenium.webdriver.common.by import By
def test_modal_open_close():
    driver = webdriver.Chrome()
    driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
    driver.find_element(By.ID, "save").click()
    modal = driver.find_element(By.CLASS_NAME, "modal-content")
    assert modal.is_displayed()