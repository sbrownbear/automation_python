from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    # Инициализация браузера
    browser = webdriver.Chrome()
    # Открыли ссылку
    browser.get(link)

    # Нашли поле ввода имени по тегу, ввели имя
    first_name = browser.find_element(By.TAG_NAME, "input")
    first_name.send_keys("Ivan")
    # Нашли поле ввода фамилии по имени, ввели фамилию
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")
    # Нашли поле ввода города по классу, ввели город
    city = browser.find_element(By.CLASS_NAME, "form-control.city")
    city.send_keys("Smolensk")
    # Нашли поле ввода страны по айди, ввели страну
    country = browser.find_element(By.ID, "country")
    country.send_keys("Russia")
    
    # Нашли button по классу и кликнули на него
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Успеваем скопировать код за 3 секунд
    time.sleep(3)
    # Закрываем браузер после всех манипуляций
    browser.quit()
    
# Не забываем оставить пустую строку в конце файла