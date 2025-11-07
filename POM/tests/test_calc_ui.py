# tests/test_calculator_ui.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    svc = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")   # comment this line if you want to see browser
    driver = webdriver.Chrome(service=svc, options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.quit()

@pytest.mark.parametrize("num1, op, num2, expected", [
    (5, "Add", "3", "8"),
    (10, "Subtract", "4", "6"),
    (7, "Multiply", "6", "42"),
    (20, "Divide", "5", "4"),
])
def test_calculator_operations(driver, num1, op, num2, expected):
    driver.get("https://testsheepnz.github.io/BasicCalculator.html")

    # enter values
    driver.find_element(By.ID, "number1Field").clear()
    driver.find_element(By.ID, "number1Field").send_keys(str(num1))
    driver.find_element(By.ID, "number2Field").clear()
    driver.find_element(By.ID, "number2Field").send_keys(str(num2))

    # select operation
    driver.find_element(By.ID, "selectOperationDropdown").send_keys(op)

    # click Calculate
    driver.find_element(By.ID, "calculateButton").click()

    # read result
    result = driver.find_element(By.ID, "numberAnswerField").get_attribute("value")
    assert result == expected
