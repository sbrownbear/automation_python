import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        # Проверка страницы авторизации
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # Проверка url страницы авторизации
    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", f"Login page link is incorrect!"

    # Проверка формы логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    # Проверка формы авторизации
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    # Регистрация нового юзера
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FIRST).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_SECOND).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
