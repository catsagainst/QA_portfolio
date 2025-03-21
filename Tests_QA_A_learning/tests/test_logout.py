from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_login_logout():
    driver.get("https://www.saucedemo.com/")

    url_before = driver.current_url
    #print(url_before)

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(3)

    #assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    burger_button = driver.find_element(By.ID, "react-burger-menu-btn")
    burger_button.click()
    time.sleep(3)

    logout_button = driver.find_element(By.ID, "logout_sidebar_link")
    logout_button.click()
    time.sleep(3)

    url_after = driver.current_url
    #print(url_after)
    assert url_before == url_after

    driver.quit()
