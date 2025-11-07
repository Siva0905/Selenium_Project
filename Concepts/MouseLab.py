from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
def mouse_hover_demo():
    driver = webdriver.Chrome()
    try:
        driver.get("https://demoqa.com/menu")
        driver.maximize_window()
        actions = ActionChains(driver)
        # Locate the main menu item
        main_item = driver.find_element(By.LINK_TEXT, "Main Item 2")
        # Get color and background-color before hover
        text_color_before = main_item.value_of_css_property("color")
        bg_color_before = main_item.value_of_css_property("background-color")
        print(f"Before Hover - Text Color: {text_color_before}, Background Color: {bg_color_before}")
        # Hover over the main menu item
        actions.move_to_element(main_item).perform()
        time.sleep(2)
        # Get color and background-color after hover
        text_color_after = main_item.value_of_css_property("color")
        bg_color_after = main_item.value_of_css_property("background-color")
        print(f"After Hover - Text Color: {text_color_after}, Background Color: {bg_color_after}")
    finally:
        driver.quit()
mouse_hover_demo()