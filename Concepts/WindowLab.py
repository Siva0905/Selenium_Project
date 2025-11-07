from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def window_handling_demo_hyr():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.hyrtutorials.com/p/window-handles-practice.html")
        parent_window = driver.current_window_handle
        print(f"Parent window: {parent_window}")
        # Click button to open new window
        new_window_btn = driver.find_element(By.ID, "newWindowBtn")
        new_window_btn.click()
        time.sleep(2)
        all_windows = driver.window_handles
        print(f"Total windows: {len(all_windows)}")
        for window in all_windows:
            if window != parent_window:
                driver.switch_to.window(window)
                print(f"Switched to: {driver.current_window_handle}")
                print(f"New window title: {driver.title}")
                print(f"New window URL: {driver.current_url}")
                # Extract content from new window
                body_text = driver.find_element(By.TAG_NAME, "body").text
                print(f"New window content:\n{body_text}")
                driver.close()
                break
        driver.switch_to.window(parent_window)
        print(f"Back to parent: {driver.title}")
    finally:
        driver.quit()
window_handling_demo_hyr()