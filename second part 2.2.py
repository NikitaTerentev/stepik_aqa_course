import time
import math
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



link = "http://suninjuly.github.io/selects1.html"
link1 = "http://suninjuly.github.io/get_attribute.html"
link2 = "http://suninjuly.github.io/execute_script.html"
link3 = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link3)



def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:

    # first task
    # num1 = browser.find_element(By.ID, "num1")
    # num2 = browser.find_element(By.ID, "num2")
    #
    # sum = str(int(num1.text) + int(num2.text))
    # select = Select(browser.find_element(By.ID, "dropdown"))
    # select.select_by_visible_text(sum)
    #
    # button = browser.find_element(By.CLASS_NAME, "btn").click()


    # second task
    # x_element = browser.find_element(By.ID, "input_value")
    # x = x_element.text
    # y = calc(x)
    # browser.execute_script("window.scrollBy(0, 120);")
    # button = browser.find_element(By.TAG_NAME, "button").click()
    # answer = browser.find_element(By.ID, "answer").send_keys(y)
    # robot_checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    # radio_button_robot = browser.find_element(By.ID, "robotsRule").click()
    # sumbit_button = browser.find_element(By.CLASS_NAME, "btn").click()

    # third task

    name = browser.find_element(By.NAME, "firstname").send_keys("abobus")
    lastname = browser.find_element(By.NAME, "lastname").send_keys("abobus")
    email = browser.find_element(By.NAME, "email").send_keys("abobus@mail.ru")
    current_dir = os.path.abspath(os.path.dirname("/Users/nikita/PycharmProjects/Stepik /test.txt"))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(5)
    browser.quit()