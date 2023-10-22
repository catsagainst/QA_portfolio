from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

driver = webdriver.Chrome()

def summa(num1,num2):
  return str(num1+num2)
def test_select():
  driver.get("https://suninjuly.github.io/selects1.html")

  num1_element = driver.find_element(By.XPATH, '//span[@id="num1"]')
  num1= int(num1_element.text)

  num2_element = driver.find_element(By.XPATH, '//span[@id="num2"]')
  num2 = int(num2_element.text)
  time.sleep(3)

  c=summa(num1,num2)

  dropdown = driver.find_element(By.ID, 'dropdown')
  dropdown.click()

  time.sleep(2)


  input1 = driver.find_element(By.XPATH, '//select[@id="dropdown"]')
  input1.send_keys(c)

  time.sleep(2)

  button = driver.find_element(By.XPATH, '//button[@type="submit"]')
  button.click()


  driver.quit()
