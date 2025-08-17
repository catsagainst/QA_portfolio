
import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="class")
def browser():
    #print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    #print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('urls', ["https://stepik.org/lesson/236895/step/1"])
                                #"https://stepik.org/lesson/236896/step/1",
                              #"https://stepik.org/lesson/236897/step/1",
                                #"https://stepik.org/lesson/236898/step/1"])
                                #"https://stepik.org/lesson/236899/step/1",
                                #"https://stepik.org/lesson/236903/step/1",
                                #"https://stepik.org/lesson/236904/step/1",
                                 #"https://stepik.org/lesson/236905/step/1"])
class TestStepik:


    def test_stepik_registration(self, browser, urls):
        browser.get(link)

        #browser.find_element(By.XPATH, '//button[@class="st-button_style_none mobile-banner__close-button"]')

        browser.implicitly_wait(10)



        form=browser.find_element(By.XPATH, '//a[@href="/lesson/236895/step/1?auth=login"]')
        form.click()
        browser.implicitly_wait(10)

        browser.find_element(By.XPATH, '//input[@id="id_login_email"]').send_keys("danilova.maria.k@gmail.com")
        browser.find_element(By.XPATH, '//input[@id="id_login_password"]').send_keys("Dramkruzok1809")

        browser.implicitly_wait(5)

        browser.find_element(By.XPATH, '//button[@type="submit"]').click()


        #element = browser.find_element(By.XPATH, '//div[@title="parametrisation test"]')

        browser.implicitly_wait(3)
        #if element.is_displayed():
            #print("Registration is successful")
        #else:
            #print("Registration is not successful")

        time.sleep(5)

        browser.find_element(By.TAG_NAME, "textarea").send_keys(str(math.log(int(time.time()))))

        #assert element.is_displayed(), 'Registration is failed'


        browser.implicitly_wait(3)
        browser.find_element(By.XPATH, '//button[@class="submit-submission"]').click()

        browser.implicitly_wait(3)


        #browser.find_element(By.XPATH, '//button[@type="button"').click()

        msg = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]')
        correct=str(msg)

        assert "Correct!" == correct, "Wrong answer"


