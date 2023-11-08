from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://magento.softwaretestingboard.com/")


def test_magento_signup():
    signup = browser.find_element(By.XPATH, "//a[contains(text(),'Create an Account')]")
    signup.click()

    time.sleep(3)

    firstname = browser.find_element(By.XPATH, '//input[@id="firstname"]')
    firstname.send_keys("Mariia")

    lastname = browser.find_element(By.XPATH, '//input[@id="lastname"]')
    lastname.send_keys("Maria")

    email = browser.find_element(By.XPATH, '//input[@id="email_address"]')
    email.send_keys("dramkruzok1@yahoo.com")

    password = browser.find_element(By.XPATH, '//input[@id="password"]')
    password.send_keys("Dramkruzok1")

    password_confirmation = browser.find_element(By.XPATH, '//input[@id="password-confirmation"]')
    password_confirmation.send_keys("Dramkruzok1")

    submit = browser.find_element(By.XPATH, '//button[@title="Create an Account"]')
    submit.click()

    time.sleep(3)




    browser.quit()
