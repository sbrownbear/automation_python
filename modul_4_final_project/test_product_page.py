import pytest
import time
from .pages.product_page import ProductPage
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By

link_login = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
link_product = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page_registration = LoginPage(browser, link_login)
        self.page_registration.open()
        email = str(time.time()) + "@fakemail.org"
        password = "673ZF4AjJk34"
        self.page_registration.register_new_user(email, password)
        self.page_registration.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        self.product_page = ProductPage(browser, link_product)
        self.product_page.open()
        self.product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        self.product_page = ProductPage(browser, link_product)
        self.product_page.open()
        self.product_page.add_product_to_basket()
        self.product_page.product_name_in_message_and_in_basket()
        self.product_page.basket_cost_equals_product_cost()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
     product_page = ProductPage(browser, link_product)
     product_page.open()
     product_page.add_product_to_basket()
     product_page.should_not_be_success_message()


def test_gust_cant_see_success_message(browser):
    product_page = ProductPage(browser, link_product)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    product_page = ProductPage(browser, link_product )
    product_page.open()
    product_page.add_product_to_basket()
    product_page.product_name_in_message_and_in_basket()
    product_page.basket_cost_equals_product_cost()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link_product)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.should_be_empty_basket_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_product)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.should_be_empty_basket_message()