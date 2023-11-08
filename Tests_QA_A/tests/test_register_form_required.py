from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random

def test_register_required():
    try:
        browser=webdriver.Chrome()
        browser.get("https://suninjuly.github.io/registration1.html")

        first_name=browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
        first_name.send_keys("Marya")

        last_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
        last_name.send_keys("Darya")

        email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
        email.send_keys("MaryaDarya@email.com")

        time.sleep(3)
        
        submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button.click()

        time.sleep(3)

        text_element = browser.find_element(By.XPATH, '//h1[contains (text(), "Congratulations!")]')
        text_element = text_element.text

        assert text_element=="Congratulations! You have successfully registered!"

    finally:
        time.sleep(5)
        browser.quit()



