from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_math():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/selects1.html")

        element1 = browser.find_element(By.XPATH, '//span[@id="num1"]')
        num1 = element1.text

        element2 = browser.find_element(By.XPATH, '//span[@id="num2"]')
        num2 = element2.text

        sleep(3)

        num3 = int(num1) + int(num2)

        dropdown_button = browser.find_element(By.XPATH, "//select[@id='dropdown']")
        dropdown_button.click()

        option = browser.find_element(By.CSS_SELECTOR, f"[value='{num3}']")
        option.click()

        sleep(3)

        submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
        submit_button.click()

    finally:
        browser.quit()

