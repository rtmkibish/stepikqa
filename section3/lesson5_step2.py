import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture(scope='function')
def browser():
  print('\nOpen Chrome')
  browser = webdriver.Chrome()
  yield browser
  print('\nClose Chrome')
  browser.quit()


class TestMainPage1:

  @pytest.mark.smoke
  def test_guest_should_see_login_link(self, browser):
    print('\nSmoke test started')
    browser.get(link)
    browser.find_element(By.XPATH, '//*[@id="login_link"]')
    print('\nSmoke test finished')

  @pytest.mark.regres
  @pytest.mark.win10
  def test_guest_should_see_basket_link_on_the_main_page(self, browser):
    print('\nRegression test started')
    browser.get(link)
    browser.find_element(By.XPATH, '//*[contains(@class, "basket-mini")]//*[@class="btn-group"]//a')
    print('\nRegression test finished')
