from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def drag_drop_demo_globalsqa():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

        # Wait for iframe and switch to it
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe.demo-frame"))
        )
        actions = ActionChains(driver)
        # Wait for source and target elements
        source = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@id='gallery']/li[1]/img"))
        )
        target = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "trash"))
        )
        # Perform drag and drop
        actions.drag_and_drop(source, target).perform()
        time.sleep(2)
        # Verify drop
        trash_contents = driver.find_element(By.ID, "trash").text
        print(f"Trash contents after drop: {trash_contents}")
    finally:
        driver.quit()
drag_drop_demo_globalsqa()