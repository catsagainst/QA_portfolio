from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import string
import random

def test_find_elements_100():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements(By.XPATH, '//input[@type="text"]')

        answer_length = 5  # Length of random string
        #for element in elements:
            #word = string.ascii_letters
            #answer = ''.join(random.choice(word) for j in range(answer_length))
            #element.send_keys(answer)
        for i in range(len(elements)):
            browser.execute_script(f'document.getElementsByTagName("input")[{i}].value = "word"') #faster than send_keys
        #for element in elements:
            #element.send_keys("hello")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        browser.quit()

    finally:
        time.sleep(5)

        browser.quit()



