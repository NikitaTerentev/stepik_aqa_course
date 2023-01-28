from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.maximize_window()

link = "http://suninjuly.github.io/wait1.html"
link1 = "http://suninjuly.github.io/wait2.html"
link2 = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link2)

def calc(x):
   return str(math.log(abs(12*math.sin(int(x)))))

price = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
btn = browser.find_element(By.ID, "book").click()
browser.execute_script("window.scrollBy(0, 300);")

x = browser.find_element(By.ID, "input_value")
y = x.text
z = calc(y)

answer = browser.find_element(By.ID, "answer").send_keys(z)
button = browser.find_element(By.ID, "solve").click()





# browser.get(link2)
# # button = browser.find_element(By.ID, "verify").click()
#
# button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


