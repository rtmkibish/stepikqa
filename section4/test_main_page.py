import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
  link = 'http://selenium1py.pythonanywhere.com/'
  page = MainPage(link, browser)
  page.open()
  page.should_be_login_link()
  page.go_to_login_page()
  login_page = LoginPage(browser.current_url, browser)
  login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
  link = 'http://selenium1py.pythonanywhere.com/'
  main_page = MainPage(link, browser)
  main_page.open()
  main_page.go_to_basket()
  basket_page = BasketPage(browser.current_url, browser, 0)
  basket_page.is_on_page()
  basket_page.should_not_be_products()
  basket_page.should_be_basket_empty_message()
