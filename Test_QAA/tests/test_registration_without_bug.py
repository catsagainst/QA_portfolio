from selenium import webdriver
from selenium.webdriver.common.by import By

import time
def test_registration_bug():
    try:

        browser=webdriver.Chrome()
        browser.get("https://suninjuly.github.io/registration2.html")

        first_name_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your name']")
        first_name_input.send_keys("My name")

        email_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email_input.send_keys("email")

        phonel_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your phone']")
        phonel_input.send_keys("1111111")

        address_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your address']")
        address_input.send_keys("Lluis Companys 12")

        time.sleep(3)

        submit_button=browser.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        time.sleep(2)

    finally:

        browser.quit()




