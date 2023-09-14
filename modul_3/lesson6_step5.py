import math, time, pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Запус теста: pytest -s -v test5.py
# Ответ: The owls are not what they seem! OvO

correct_answer = "Correct!"

def calc():
    answer = math.log(int(time.time()))
    return str(answer)

@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    # browser.implicitly_wait(30)
    yield browser
    browser.quit()

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1"])

class TestMainPage5():
    def test_lesson4(self, browser, links):
        browser.get(links)
        time.sleep(7)

        # Авторизовались
        browser.find_element(By.ID, "ember33").click()
        time.sleep(5)
        browser.find_element(By.NAME, "login").send_keys("brownbeer@mail.ru")
        browser.find_element(By.NAME, "password").send_keys("Ifevep35))")
        browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
        time.sleep(5)

        # Поп-апа с авторизацией больше нет
        EC.visibility_of_element_located((By.ID, "ember93"))
        time.sleep(5)

        browser.find_element(By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(calc())
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        fact_answer = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        assert fact_answer == correct_answer, f"Answer incorrect! Fact answer: {fact_answer}, expected: {correct_answer}"

