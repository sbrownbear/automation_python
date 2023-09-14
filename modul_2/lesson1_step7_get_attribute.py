from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    treasure_value = browser.find_element(By.ID, "treasure")
    attribute_treasure = treasure_value.get_attribute("valuex")
   
    x = attribute_treasure
    y = calc(x)

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(y)

    checkbox_status = browser.find_element(By.ID, "robotCheckbox")
    checkbox_status.click()

    radiobutton_status = browser.find_element(By.ID, "robotsRule") 
    radiobutton_status.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
