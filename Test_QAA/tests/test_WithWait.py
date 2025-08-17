from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()


def test_verify():
    browser.get("http://suninjuly.github.io/wait1.html")

    time.sleep(5) #waiting period!!!

    verify_button = browser.find_element(By.XPATH, '//button[@id="verify"]')
    verify_button.click()

    browser.implicitly_wait(5)

    message = browser.find_element(By.XPATH, '//div[@id = "verify_message"]')
    message_text = message.text


    assert message_text == "Verification was successful!"


    browser.quit()

    #button = browser.find_element(By.ID, "verify")
    #button.click()
    #message = browser.find_element(By.ID, "verify_message")

    #assert "successful" in message.text
