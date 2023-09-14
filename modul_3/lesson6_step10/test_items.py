import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_exist_add_to_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    # time.sleep(30)
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket").is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'
