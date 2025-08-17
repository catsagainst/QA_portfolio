import time

import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, '//a[@id="login_link"]')
        time.sleep(5)

    def test_guest_should_see_find_button(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.implicitly_wait(5)
        browser.find_element(By.XPATH, '//input[@type="submit"]')
        time.sleep(5)