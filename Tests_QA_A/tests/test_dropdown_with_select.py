import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")


def summa(num1, num2):
    return num1 + num2


def test_select_dropdown():
    num1_element = browser.find_element(By.XPATH, '//span[@id="num1"]')
    num1 = int(num1_element.text)

    num2_element = browser.find_element(By.XPATH, '//span[@id="num2"]')
    num2 = int(num2_element.text)

    c = summa(num1, num2)
    time.sleep(3)

    select = Select(browser.find_element(By.TAG_NAME, "select"))

    #select.select_by_value(f"[value='{c}']").click()
    browser.find_element(By.CSS_SELECTOR, (f"[value='{c}']")).click()
    time.sleep(1)

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()

    browser.quit()

    # select.select_by_visible_text("text")
    # select.select_by_index(index)

