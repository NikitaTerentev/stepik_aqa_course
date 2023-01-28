import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # link - Рабочий линк
    link = "http://suninjuly.github.io/registration1.html"
    # link1 - Получаем ошибку
    link1 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    # Код, который заполняет обязательные поля
    first_name = browser.find_element(By.XPATH, "//input[contains(@placeholder,'first')]").send_keys("Aboba")
    last_name = browser.find_element(By.CSS_SELECTOR, ".form-control.second").send_keys("Aboba")
    email = browser.find_element(By.CSS_SELECTOR, ".form-control.third").send_keys("abobs@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


