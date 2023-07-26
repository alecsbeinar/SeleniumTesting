from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import *

site = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(site)

    x = float(browser.find_element(By.ID, "input_value").text)
    value_answer = log(abs(12*sin(x)))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(value_answer)

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
