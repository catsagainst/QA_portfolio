import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")
def summa(num1,num2):
  return str(num1+num2)

def test_select_dropdown():
    num1_element =browser.find_element(By.XPATH, '//span[@id="num1"]')
    num1 = int(num1_element.text)

    num2_element = browser.find_element(By.XPATH, '//span[@id="num2"]')
    num2 = int(num2_element.text)
    time.sleep(3)

    c = summa(num1, num2)

    browser.find_element(By.TAG_NAME, "select").click()
    time.sleep(4)
    browser.find_element(By.CSS_SELECTOR, "[value='" + c + "']").click()

    time.sleep(3)

    browser.quit()