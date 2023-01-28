import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/alert_accept.html"
link2 = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link2)

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

try:

    #fisrt part
    # btn = browser.find_element(By.CLASS_NAME, "btn").click()
    # alert = browser.switch_to.alert.accept()
    # x = browser.find_element(By.ID, "input_value")
    # y = x.text
    # z = calc(y)
    # answer = browser.find_element(By.ID, "answer").send_keys(z)
    # second_btn = browser.find_element(By.CLASS_NAME, "btn").click()

    btn = browser.find_element(By.CLASS_NAME, "btn").click()
    first_winwon = browser.window_handles[0]
    new_window = browser.window_handles[1]
    jump_to_new_window = browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value")
    y = x.text
    z = calc(y)
    answer = browser.find_element(By.ID, "answer").send_keys(z)
    second_btn = browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(10)
    browser.quit()