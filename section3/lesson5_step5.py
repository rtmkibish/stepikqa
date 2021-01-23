import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='function')
def browser():
  browser = webdriver.Chrome()
  yield browser
  browser.quit()


class TestMainPage1:

    def test_guest_should_see_login_link(self, browser):
      browser.get(link)
      browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
      browser.get(link)
      browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.skip
    def test_dummy_test(self):
      """This test will be skiped as it is marked as skip"""
      pass

    @pytest.mark.xfail(reason='bug fix is in progress')
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
      browser.get(link)
      browser.find_element_by_css_selector("button.favorite")
