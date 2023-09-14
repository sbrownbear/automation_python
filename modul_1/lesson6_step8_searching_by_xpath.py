from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    # Инициализация браузера, открытие ссылки
    browser = webdriver.Chrome()
    browser.get(link)

    # Нашли поле ввода имени
    name = browser.find_element(By.XPATH, "//input[@name='first_name']")
    name.send_keys("Sergey")
    # Нашли поле ввода фамилии
    last_name = browser.find_element(By.XPATH, "//input[@name='last_name']")
    last_name.send_keys("Konoplev")
    # Нашли поле ввода города
    city = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    city.send_keys("Penza")
    # Нашли поле ввода страны
    country = browser.find_element(By.XPATH, "//input[@id='country']")
    country.send_keys("Russia")

    # Нашли button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
