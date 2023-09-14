from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
import time
import math

# Раскрывающиеся (выпадающие) списки. Пример выполнения кода с библиотекой Select.

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Нашли два элемента и их сумму
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    sum = num1 + num2

    # Выбрали в списке полученную сумму (через спец. библиотеку)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    # Кликнули на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()