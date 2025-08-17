

num_value = browser.find_element(By.XPATH, '//span[@id="input_value"]')
x = num_value.text
x = int(x)

import calc

num = calc.calc(x)

answer = browser.find_element(By.XPATH, '//input[@id="answer"]')
answer.send_keys(num)

submit = browser.find_element(By.XPATH, '//button[@type="submit"]')
submit.click()

time.sleep(5)