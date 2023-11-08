
import time

#from selenium import webdriver
#browser = webdriver.Chrome()
#browser.execute_script("document.title='Script executing';alert('Vamos a estudiar!');")

#time.sleep(4)

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

time.sleep(3)
button.click()