import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exception1():
  try:
    browser = webdriver.Chrome()
    browser.get('http://selenium1py.pythonanywhere.com/')
    with pytest.raises(NoSuchElementException):
      browser.find_element(By.XPATH, '//button[contains(@class, "btn")]')
      pytest.fail('Must be no Send button')
  finally:
    browser.quit()

def test_exception2():
  try:
    browser = webdriver.Chrome()
    browser.get('http://selenium1py.pythonanywhere.com/')
    with pytest.raises(NoSuchElementException):
      browser.find_element(By.XPATH, '//no_such_button')
      pytest.fail('Must be no Send button')
  finally:
    browser.quit()
