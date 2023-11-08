import selenium
from selenium.webdriver.common.by import By
import time

driver = selenium.webdriver.Chrome()

def test_addToCart():
    driver.get("https://www.saucedemo.com/")

    #registration
    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)

    #adding to the cart
    item_button1 = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    item_button1.click()

    time.sleep(5)
    item_button2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    item_button2.click()

    #cart
    cart_button = driver.find_element(By.XPATH, '//span[@class ="shopping_cart_badge"]')
    cart_button.click()

    #text_before = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')


    #text_after = driver.find_element(By.CSS_SELECTOR, 'a[id="item_4_title_link"] > div[class="inventory_item_name"]')

    #assert text_before==text_after

    time.sleep(5)

    #assert driver.find_elements(By.XPATH, '//span[@class="shopping_cart_badge"][contains(text(),"2")]')
    goods = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
    print(len(goods))
    assert len(goods) == 2 #assert quantity with find_elements (and len())

    time.sleep(2)
    checkout_button = driver.find_element(By.XPATH, '//button[@id="checkout"]')
    checkout_button.click()


    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"
    driver.quit()





