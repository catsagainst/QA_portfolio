from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)


import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def test_sinViewSubmit():
    num_value=browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x=num_value.text
    x=int(x)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    num=calc(x)


    answer = browser.find_element(By.XPATH, '//input[@id="answer"]')
    answer.send_keys(num)

    robotCheck = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    robotCheck.click()

    robotsRule = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')
    robotsRule.click()

    submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()

    time.sleep(5)

    browser.quit()




