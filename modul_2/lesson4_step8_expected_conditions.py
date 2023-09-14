from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Пример ожидания

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Дождаться, когда цена дома уменьшится до 100 баксов
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))

    # Нажать на кнопку "Забронировать"
    book = browser.find_element(By.ID, "book")
    book.click()

    # Решить уже известную нам математическую задачу (используйте ранее написанный код)
    num = int(browser.find_element(By.ID, "input_value").text)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(str(math.log(abs(12*math.sin(num)))))

    # Клик button
    button = browser.find_element(By.ID, 'solve')
    button.click()

finally:
    time.sleep(7)
    browser.quit()