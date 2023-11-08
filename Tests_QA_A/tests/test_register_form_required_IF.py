from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random

def test_register_required():
    try:
        browser=webdriver.Chrome()
        browser.get("https://suninjuly.github.io/registration1.html")

        elements = browser.find_elements(By.XPATH,'//input[@type="text" and @required]')
        for element in elements:
            element.send_keys("Test text")

        time.sleep(3)

        submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button.click()

        time.sleep(3)

        text_element = browser.find_element(By.XPATH, '//h1[contains (text(), "Congratulations!")]')
        text_element = text_element.text

        assert text_element == "Congratulations! You have successfully registered!"

    finally:
        time.sleep(5)
        browser.quit()

#//input[@type="text" and @required]
#input:required