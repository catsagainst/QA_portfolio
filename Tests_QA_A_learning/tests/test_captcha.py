from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()


def test_captcha():
  driver.get("https://suninjuly.github.io/math.html")
  x_element = driver.find_element(By.XPATH, '//span[@id="input_value"]')
  x = x_element.text
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

  print(answer_field)



  driver.quit()