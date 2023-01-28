import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


# 1

link = "https://suninjuly.github.io/math.html"
link1 = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link1)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     people_attribute = browser.find_element(By.ID, "peopleRule")
#     check_att = people_attribute.get_attribute("checked")
#     print("value of people radio: ", check_att)
#     assert check_att == "true", "People radio is not selected by default"


# try:
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#     answer = browser.find_element(By.ID, "answer").send_keys(y)
#     check_box = browser.find_element(By.ID, "robotCheckbox").click()
#     radio_button = browser.find_element(By.ID, "robotsRule").click()
#     button = browser.find_element(By.CLASS_NAME, "btn").click()

try:

    treasure = browser.find_element(By.ID, "treasure")
    get_attr = treasure.get_attribute("valuex")
    y = calc(get_attr)
    answer = browser.find_element(By.ID, "answer").send_keys(y)
    check_box = browser.find_element(By.ID, "robotCheckbox").click()
    radio_butt = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(3)
    browser.quit()