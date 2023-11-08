from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_login_form():
    driver.get("https://www.litecart.net/")


    login_button = driver.find_element(By.XPATH, "//li[@class='languages dropdown']")
    login_button.click()

    login_button = driver.find_element(By.XPATH, "//a[@hreflang='es']")
    login_button.click()



    time.sleep(5)
    assert driver.current_url == "https://www.litecart.net/es/"

    driver.quit()