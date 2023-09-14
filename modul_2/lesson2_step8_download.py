from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Пример загрузки файла с помощью библиотеки os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ввели имя
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Sergey")
    # Ввели Фамилию
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Konoplev")
    # Ввели имя email
    email = browser.find_element(By.NAME, "email")
    email.send_keys("sergeyKonoplev@gmail.com")

    # with open("file_example.txt", "w") as file:
    #     content = file.write("automationbypython")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file_example.txt")
    browser.find_element(By.ID, "file").send_keys(file_path)

    # Нашли button и кликнули на него
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

