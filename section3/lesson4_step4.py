import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture
def browser():
  print('Launching the browser...')
  browser = webdriver.Chrome()
  yield browser
  print('Closing the browser...')
  browser.quit()

@pytest.fixture(scope='class')
def browser2():
  print('launching the browser...')
  browser = webdriver.Chrome()
  yield browser
  print('Closing the browser...')
  browser.quit()

@pytest.fixture(autouse=True)
def dummy():
  print('I will run before each test automaticaly without passing me and invokation')


class TestMainPage1:
  def test_guest_should_see_login_link(self, browser):
    browser.get(link)
    browser.find_element(By.XPATH, '//*[@id="login_link"]')

  def test_guest_should_see_basket_link_on_the_main_page(self, browser):
    browser.get(link)
    browser.find_element(By.XPATH, '//div[contains(@class, basket-mini)]//*[@class="btn-group"]//a')


class TestMainPage2:
  def test_guest_should_see_login_link(self, browser2):
    print("start test1")
    browser2.get(link)
    browser2.find_element_by_css_selector("#login_link")
    print("finish test1")

  def test_guest_should_see_basket_link_on_the_main_page(self, browser2):
    print("start test2")
    browser2.get(link)
    browser2.find_element_by_css_selector(".basket-mini .btn-group > a")
    print("finish test2")
