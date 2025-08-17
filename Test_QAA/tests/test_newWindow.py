import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = selenium.webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

#def calc(x):
  #return str(math.log(abs(12*math.sin(int(x)))))

def test_newWindow():

    submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()

    time.sleep(3)

    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]

    browser.switch_to.window(new_window)

    num_value = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = num_value.text
    x = int(x)

    import calc

    num = calc.calc(x)

    answer = browser.find_element(By.XPATH, '//input[@id="answer"]')
    answer.send_keys(num)

    submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()

    time.sleep(5)

    browser.quit()




