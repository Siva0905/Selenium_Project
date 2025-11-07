from selenium import webdriver
from selenium.webdriver.common.by import By
def test_form_validation():
    driver = webdriver.Chrome()
    driver.get("https://www.w3schools.com/html/html_forms.asp")

    input_box = driver.find_element(By.ID, "fname")
    input_box.clear()
    input_box.send_keys("John")

    submit = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit.click()

    # You can assert based on expected behavior after submission
    assert input_box.get_attribute("value") == "John"

    driver.quit()
