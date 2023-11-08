import time

from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")


def test_math():
    element1 = browser.find_element(By.CSS_SELECTOR, '#num1')
    num1 = element1.text

    element2 = browser.find_element(By.CSS_SELECTOR, '#num2')
    num2 = element2.text

    time.sleep(3)

    num3 = int(num1) + int(num2)

    dropdown_button = browser.find_element(By.XPATH, "//select[@id='dropdown']")
    dropdown_button.click()

    browser.find_element(By.CSS_SELECTOR, "[value='" + num3 + "']").click()

    time.sleep(3)

    submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()

    browser.quit()
