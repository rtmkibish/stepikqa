import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


def test_guest_can_add_product_to_basket(browser):
  product_page = ProductPage('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019', browser)
  product_page.open()
  product_page.add_product_to_basket()
  product_page.solve_quiz_and_get_code()
  product_page.should_be_added_correct_product_name()
  product_page.should_message_price_be_equal_to_product_price()
  product_page.should_basket_price_equal_to_product_price()

@pytest.mark.parametrize('link', [
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
  ])
def test_guest_can_add_product_to_basket_parametrized(browser, link):
  product_page = ProductPage(link, browser)
  product_page.open()
  product_page.add_product_to_basket()
  product_page.solve_quiz_and_get_code()
  product_page.should_be_added_correct_product_name()
  product_page.should_message_price_be_equal_to_product_price()
  product_page.should_basket_price_equal_to_product_price()

@pytest.mark.xfail(reason='Fail due to the stepik task condition')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
  product_page = ProductPage('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019', browser, 0)
  product_page.open()
  product_page.add_product_to_basket()
  product_page.solve_quiz_and_get_code()
  product_page.is_not_product_added_message()

def test_guest_cant_see_success_message(browser):
  product_page = ProductPage('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019', browser, 0)
  product_page.open()
  product_page.is_not_product_added_message()

@pytest.mark.xfail(reason='Fail due to the stepik task condition')
def test_message_disappeared_after_adding_product_to_basket(browser):
  product_page = ProductPage('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019', browser, 0)
  product_page.open()
  product_page.add_product_to_basket()
  product_page.solve_quiz_and_get_code()
  product_page.is_product_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
  link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
  page = ProductPage(browser, link)
  page.open()
  page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
  link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
  page = ProductPage(link, browser)
  page.open()
  page.go_to_login_page()
  login_page = LoginPage(browser.current_url, browser)
  login_page.is_on_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
  link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
  product_page = ProductPage(link, browser)
  product_page.open()
  product_page.go_to_basket()
  basket_page = BasketPage(browser.current_url, browser, 0)
  basket_page.is_on_page()
  basket_page.should_not_be_products()
  basket_page.should_be_basket_empty_message()
