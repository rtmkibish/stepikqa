from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
  """
  Represents the Login Page
  """

  def should_be_login_page(self):
    self.should_be_login_url()
    self.should_be_login_form()
    self.should_be_register_form()

  def should_be_login_url(self):
    assert self.is_on_page(), 'Should be on the login page'

  def should_be_login_form(self):
    assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Should be login form'

  def should_be_register_form(self):
    assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Should be register form'
