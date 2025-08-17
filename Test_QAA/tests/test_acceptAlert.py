import selenium
from selenium.webdriver.common.by import By
import time
import math

browser = selenium.webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_acceptAlert():

    submit=browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()

    time.sleep(2)

    confirm = browser.switch_to.alert
    confirm.accept()
    
    #confirm.dismiss()
    #prompt = browser.switch_to.alert
    #prompt.send_keys("My answer")
    #prompt.accept()
    #alert = browser.switch_to.alert
    #alert.accept()
    #alert = browser.switch_to.alert
    #alert_text = alert.text


    num_value = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = num_value.text
    x = int(x)

    num = calc(x)

    answer = browser.find_element(By.XPATH, '//input[@id="answer"]')
    answer.send_keys(num)


    submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()

    time.sleep(5)

    browser.quit()




