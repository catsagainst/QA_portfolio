from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")

link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()

try:

    #browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Mariia")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Danilkina")
    input3 = browser.find_element(By.XPATH, '//input[@class="form-control city"]')
    input3.send_keys("Barselonsk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Spagna")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
#link = browser.find_element(By.PARTIAL_LINK_TEXT, "Math")
#link.click()

time.sleep(3)

browser.quit()
