from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")


import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def test_chest():
    chest=browser.find_element(By.XPATH, '//img[@id="treasure"]')
    x = chest.get_attribute("valuex")
    x=int(x)

    num = calc(x)

    answer=browser.find_element(By.XPATH, '//input[@id="answer"]')
    answer.send_keys(num)

    time.sleep(3)

    robotCheck = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    robotCheck.click()

    robotsRule = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')
    robotsRule.click()

    time.sleep(5)

    submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()


    time.sleep(4)


