from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()


def test_captcha2():
  driver.get("http://suninjuly.github.io/get_attribute.html")
  element = driver.find_element(By.XPATH, '//img[@id="treasure"]')
  x_element=element.get_attribute('valuex')
  x = x_element
  y = calc(x)

  answer_field = driver.find_element(By.XPATH, '//input[@id="answer"]')
  answer_field.send_keys(y)
  time.sleep(3)

  robot_checkbox=driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
  robot_checkbox.click()
  time.sleep(3)


  robots_rule = driver.find_element(By.XPATH, '//input[@id="robotsRule"]')
  robots_rule.click()
  time.sleep(3)

  button = driver.find_element(By.XPATH, '//button[@type="submit"]')
  button.click()

  print(x)



  driver.quit()