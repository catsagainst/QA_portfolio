from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_login_form():
    driver.get("https://www.litecart.net/")
    langs=["es", "en", "it", "lt", "fr", "fi", "ar", "el", "vi", "hu", "da", "tr", "nl", "sv", "fa", "th", "id", "de"]

    for i in langs:
        login_button = driver.find_element(By.XPATH, "//li[@class='languages dropdown']")
        login_button.click()

        login_button = driver.find_element(By.XPATH, f"//a[@hreflang='{i}']")
        login_button.click()

        time.sleep(1)
        assert driver.current_url == f"https://www.litecart.net/{i}/"

    driver.quit()