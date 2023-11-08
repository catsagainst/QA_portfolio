from selenium import webdriver
from selenium.webdriver.common.by import By

import time
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/simple_form_find_task.html"

def test_form_try():
    try:

        browser.get(link)

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Mariia")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Danilkina")
        input3 = browser.find_element(By.XPATH, '//input[@class="form-control city"]')
        input3.send_keys("Barselonsk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Spagna")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        time.sleep(15)
        browser.quit()