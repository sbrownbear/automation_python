from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"
answer = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Переходим по зашифрованной ссылке
    button = browser.find_element(By.LINK_TEXT, answer)
    button.click()

    # Заполняем форму
    name = browser.find_element(By.TAG_NAME, "input")
    name.send_keys("Sergey")
    last_name = browser.find_element(By.NAME, "last_name")
    last_name.send_keys("Konoplev")
    city = browser.find_element(By.CLASS_NAME, "form-control.city")
    city.send_keys("Penza")
    country = browser.find_element(By.ID, "country")
    country.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
    