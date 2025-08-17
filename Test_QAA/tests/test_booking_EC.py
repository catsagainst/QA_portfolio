from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def test_booking():

    try:
        button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

        book = browser.find_element(By.ID, "book")
        book.click()

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

    finally:

        browser.quit()


