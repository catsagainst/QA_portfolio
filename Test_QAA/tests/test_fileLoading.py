from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import os

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/file_input.html")

def test_file_input():

    firstname = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    firstname.send_keys("Jan")

    lastname = browser.find_element(By.XPATH,'//input[@name="lastname"]')
    lastname.send_keys("Jan")

    email = browser.find_element(By.XPATH, '//input[@name="email"]')
    email.send_keys("Jan@Jan")

    time.sleep(2)

    file = browser.find_element(By.XPATH, '//input[@id="file"]')
    #file.send_keys("/Users/mariadanilova/Downloads/test empty file.txt") #1st way

    directory = "/Users/mariadanilova/Downloads/"
    file_name = "test empty file.txt"
    file_path = os.path.join(directory, file_name)

    file.send_keys(file_path) #2nd way

    time.sleep(3)

    submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submit.click()

    time.sleep(4)

    browser.quit()





