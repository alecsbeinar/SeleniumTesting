from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

site = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(site)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.trollface")
    button.click()
    browser.switch_to.window(browser.window_handles[1])

    x = float(browser.find_element(By.ID, "input_value").text)
    value_answer = log(abs(12*sin(x)))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(value_answer)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
