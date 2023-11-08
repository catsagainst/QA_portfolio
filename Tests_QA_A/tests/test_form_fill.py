from selenium import webdriver
from selenium.webdriver.common.by import By

import time

browser=webdriver.Chrome()
#browser.get("https://suninjuly.github.io/simple_form_find_task.html")
browser.get("http://suninjuly.github.io/find_xpath_form")

def test_form_fill():
    first_name=browser.find_element(By.XPATH,'//input[@name="first_name"]')
    first_name.send_keys("Mariia")

    time.sleep(2)

    last_name = browser.find_element(By.XPATH, '//input[@name="last_name"]')
    last_name.send_keys("Danilova")

    time.sleep(2)

    city=browser.find_element(By.XPATH, '//input[@class="form-control city"]')
    city.send_keys("Barcelona")

    time.sleep(2)

    country = browser.find_element(By.XPATH, "//input[@id='country']")
    country.send_keys("Spain")

    time.sleep(5)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

    browser.quit()

