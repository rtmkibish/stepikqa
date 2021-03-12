from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
  link = 'http://selenium1py.pythonanywhere.com/'
  page = MainPage(link, browser)
  page.open()
  page.should_be_login_link()

def test_guest_see_login_page(browser):
  link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
  page = LoginPage(link, browser)
  page.open()
  page.should_be_login_page()
