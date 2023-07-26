from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
from math import *

site = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(site)
    # говорим WebDriver ждать все элементы в течение 5 секунд
    # browser.implicitly_wait(5)

    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 13).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    button.click()

    x = float(browser.find_element(By.ID, "input_value").text)
    value_answer = log(abs(12*sin(x)))

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(value_answer)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
