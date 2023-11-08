from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://magento.softwaretestingboard.com/")


def test_magento_signup():
    signin = browser.find_element(By.XPATH, "//a[contains(text(),'Sign In')]")
    signin.click()

    time.sleep(3)

    email = browser.find_element(By.XPATH, '//input[@name="login[username]"]')
    email.send_keys("dramkruzok2@yahoo.com")

    password = browser.find_element(By.XPATH, '//input[@id="login[password]"]')
    password.send_keys("Dramkruzok1")

    submit = browser.find_element(By.XPATH, '//button[@id="send2"]')
    submit.click()

    time.sleep(3)




    browser.quit()
