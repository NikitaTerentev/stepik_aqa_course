import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):

    # link1 - Получаем ошибку
    link1 = "http://suninjuly.github.io/registration2.html"

    def test_abs01(self):

        # link - Рабочий линк
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get(link)
        first_name = browser.find_element(By.XPATH, "//input[contains(@placeholder,'first')]").send_keys("Aboba")
        last_name = browser.find_element(By.CSS_SELECTOR, ".form-control.second").send_keys("Aboba")
        email = browser.find_element(By.CSS_SELECTOR, ".form-control.third").send_keys("abobs@gmail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Success")


    def test_abs02(self):

            # link1 - Получаем ошибку
            link1 = "http://suninjuly.github.io/registration2.html"

            browser = webdriver.Chrome()
            browser.maximize_window()
            browser.get(link1)
            first_name = browser.find_element(By.XPATH, "//input[contains(@placeholder,'first')]").send_keys("Aboba")
            last_name = browser.find_element(By.CSS_SELECTOR, ".form-control.second").send_keys("Aboba")
            email = browser.find_element(By.CSS_SELECTOR, ".form-control.third").send_keys("abobs@gmail.com")
            button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

            welcome_text = welcome_text_elt.text

            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Success")

if __name__ == "__main__": unittest.main()