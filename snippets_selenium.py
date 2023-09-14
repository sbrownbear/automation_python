from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get(link)

# Работа со списками

# <label for="dropdown">Выберите язык программирования:</label>
# <select id="dropdown" class="custom-select">
#      <option selected>--</option>
#      <option value="1">Python</option>
#      <option value="2">Java</option>
#      <option value="3">JavaScript</option>
# </select>

# Вариант первый
browser.find_element(By.TAG_NAME, "select").click() # Список раскрылся
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click() # Выбрали нужный элемент

# Или
browser.find_element(By.CSS_SELECTOR, "[value='1']").click() # Выбрали нужный элемент


# Вариант второй
from selenium.webdriver.support.ui import Select # Импортнули специальный класс Select из библиотеки WebDriver

select = Select(browser.find_element(By.TAG_NAME, "select")) # Инициализировали новый объект, передав в него WebElement с тегом select
select.select_by_value("1") # Ищем элемент с текстом "Python"

# Или
select.select_by_visible_text("text") # Ищет элемент по видимому тексту
select.select_by_index(1) # Ищет элемент по его индексу или порядковому номеру
# Индексация начинается с нуля. Опция с индексом 0 в данном примере имеет значение по умолчанию равное "--"




# Метод execute_script
execute_script(javascript_code);
browser.execute_script("alert('Robots at work');")

# Можно выполнить сразу несколько инструкций
browser.execute_script("document.title='Script executing';alert('Robots at work');")

# Проскроллить нужный элемент, чтобы он точно стал видимым
"return arguments[0].scrollIntoView(true);"

# Кликнуть на перекрытую кнопку
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# Вариант второй
button = document.getElementsByTagName("button")[0];
button.scrollIntoView(true);

# Можно проскроллить всю страницу целиком на 100 пикселей
browser.execute_script("window.scrollBy(0, 100);")




# Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
# Три способа задать путь к файлу:

# 1. вбить руками
element.send_keys("/home/user/stepik/Chapter2/file_example.txt")


# 2. задать с помощью переменных
# Указывая директорию, где лежит файл.txt
# В конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# Имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# Собираем путь к файлу
file_path = os.path.join(directory, file_name)
# Отправляем файл
element.send_keys(file_path)


# 3.путь автоматизатора.
# Если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# Импортируем модуль
import os
# Получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# Имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# Получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# Отправляем файл
element.send_keys(file_path)

# Итоговый код:
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)




# 2.3. Работа с окнами
# Виды: alert (ок), confirm (ок, отмена), prompt (доп.поле ввода, ок, отмена)

#Работа с alert
alert = browser.switch_to.alert
alert.accept()
#Получить текст из alert
alert = browser.switch_to.alert
alert_text = alert.text

#Работа с comfirm
confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

#Работа с prompt
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()




# 2.3. Переход на новую вкладку браузера switch_to.window
browser.switch_to.window(browser.window_handles[1]) # Перейти на следующую страницу



# Явные и неявные ожидания
# Неявное ожидание (Implicit wait) WebDriver ищет каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

#Явное ожидание (Explicit Waits) проверяет в течение 5 секунд, пока кнопка не станет кликабельной
#Можно использовать until_not
from selenium.webdriver.support import expected_conditions as EC
button = WebDriverWait(browser, 5).until(
                EC.element_to_be_clickable((By.ID, "verify")))




# Глава 3
# Пирамида тестирования
# 1. Ручные исследовательские тесты 2. Автоматизированные end-to-end тесты 3. Интеграционные тесты 4. Юнит-тесты


# Составные сообщения об ошибках
catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
	f"Wrong language, got {catalog_text} instead of 'Каталог'"
    
# Пример кода проверки
def test_input_text(expected_result, actual_result):
    assert (expected_result == actual_result), \
                (f"expected {expected_result}, got {actual_result}")

# Пример кода проверки 2
def test_substring(full_string, substring):
    assert (substring in full_string), (f"expected '{substring}' to be substring of '{full_string}'")



# Pytest
pytest scripts/selenium_scripts
# найти все тесты в директории scripts/selenium_scripts
pytest test_user_interface.py
# найти и выполнить все тесты в файле 
pytest scripts/drafts.py::test_register_new_user_parametrized
# найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить





# Маркировка тестов и пропуск тестов

# Запустится только smoke:
@pytest.mark.smoke : pytest -s -v -m smoke test_fixture.py

# Запуска всех тестов, не отмеченных как smoke:
@pytest.mark.smoke : pytest -s -v -m "not smoke" test_fixture.py

# Запуск тестов с разными маркировками:
@pytest.mark.smoke
@pytest.mark.regression : pytest -s -v -m "smoke or regression" test_fixture.py

# Запуск тестов имеющих несколько маркировок:
@pytest.mark.smoke
@pytest.mark.win10 : pytest -s -v -m "smoke and win10" test_fixture.py

# Пропуск тестов:
@pytest.mark.skip : pytest -s -v  test_fixture.py

# Помечать тест как ожидаемо падающий(пометка:XFAIL):
# упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный
# Когда баг починят, мы это узнаем, так как тест будет отмечен как XPASS
@pytest.mark.xfail : pytest -rx -v test_fixture.py

# reason - Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rX
@pytest.mark.xfail(reason="fixing this bug right now") : pytest -rX -v test_fixture.py

# Параметр strict
# Ни XFAIL, ни XPASS по умолчанию не приводят к падению всего набора тестов.
# Но это можно изменить, установив параметру strict значение True:
# В этом случае, если тест будет неожиданно пройден (XPASS),
# то это приведет к падению всего тестового набора
@pytest.mark.xfail(strict=True) : pytest -rX -v test_fixture.py
