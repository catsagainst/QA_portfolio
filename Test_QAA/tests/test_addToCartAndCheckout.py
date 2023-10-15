from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

def test_addToCart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)

    item_button = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    item_button.click()

    cart_button = driver.find_element(By.XPATH, '//span[@class ="shopping_cart_badge"]')
    cart_button.click()

    text_before = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')


    text_after = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')

    assert text_before==text_after

    time.sleep(5)

    assert driver.find_elements(By.XPATH, "//div[@class='cart_quantity'][contains(text(),'1')]")

    checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
    checkout_button.click()


    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    driver.quit()



    cart_button = driver.find_element(By.XPATH, '//span[@class ="shopping_cart_badge"]')
    cart_button.click()

    time.sleep(5)

    assert driver.find_elements(By.XPATH, "//div[@class='cart_quantity'][contains(text(),'1')]")

    checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
    checkout_button.click()


    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    driver.quit()