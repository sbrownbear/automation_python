from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Функция, которая считает ответ
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Нашли число по id, поле по классу и ввели число
    x = browser.find_element(By.ID, 'input_value')
    num = browser.find_element(By.CLASS_NAME, 'form-control')
    num.send_keys(calc(int(x.text)))
    
    # Кликнули чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    
    # Кликнули радиобатон
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    
    # Кликнули submit
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()


