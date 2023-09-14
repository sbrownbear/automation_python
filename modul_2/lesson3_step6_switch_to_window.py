from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Пример перехода на новую вкладку браузера switch_to.window

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Клик button
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(1)

    # Перешли на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # Нашли число
    num = int(browser.find_element(By.ID, "input_value").text)

    # Нашли поле ввода ответа и записали ответ
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(str(math.log(abs(12*math.sin(num)))))
    
    # Клик button
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(5)
    browser.quit()