from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который заполняет обязательные поля
    browser.find_element_by_css_selector('div.first_block input.first').send_keys('Sergey')
    browser.find_element_by_css_selector('div.first_block input.second').send_keys('Konoplev')
    browser.find_element_by_css_selector('div.first_block input.third').send_keys('fgbdb@mail.ru')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # Находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # Записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # С помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # Закрываем браузер после всех манипуляций
    browser.quit()