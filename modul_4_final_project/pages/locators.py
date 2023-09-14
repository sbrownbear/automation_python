from selenium.webdriver.common.by import By

# Базовые локаторы
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs>span>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

# Локаторы с главной страницы
class MainPageLocators:
    pass

# Локаторы со страницы корзины
class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

# Локаторы со страницы авторизации
class LoginPageLocators:
     LOGIN_FORM =  (By.CSS_SELECTOR, "#login_form")
     REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
     REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
     REGISTER_PASSWORD_FIRST = (By.CSS_SELECTOR, "#id_registration-password1")
     REGISTER_PASSWORD_SECOND = (By.CSS_SELECTOR, "#id_registration-password2")
     REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")

# Локаторы со страницы продукта
class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages>div:nth-child(1)>.alertinner>strong")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main>.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
