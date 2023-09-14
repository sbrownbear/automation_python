from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Метод execute_script, пример прокрутки до нужного элемента

link = "https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Нашли число
    num = int(browser.find_element(By.ID, "input_value").text)

    # Нашли поле ввода ответа, скролл до нужного элемента и записали ответ
    answer = browser.find_element(By.ID, "answer")
    browser.execute_script('return arguments[0].scrollIntoView(true);', answer)
    answer.send_keys(str(math.log(abs(12*math.sin(num)))))

    # Нашли checkbox, скролл до нужного элемента и поставили галочку
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script('return arguments[0].scrollIntoView(true);', checkbox)
    checkbox.click()

    # browser.execute_script("window.scrollBy(0, 100);") - как вариант

    # Нашли radiobutton, скролл до нужного элемента и поставили галочку
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script('return arguments[0].scrollIntoView(true);', radiobutton)
    radiobutton.click()
    
    # Нашли button, скролл до нужного элемента и кликнули на него
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()