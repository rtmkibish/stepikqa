import random
import string
import time

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

  def register_new_user(self):
    letters = string.ascii_lowercase
    email = ''.join(random.choice(letters) for _ in range(10)) + '@fakemail.org'
    password = ''.join(random.choice(letters) for _ in range(10))

    email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
    email_field.send_keys(email)
    password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD)
    password_field.send_keys(password)
    confirm_password_field = self.browser.find_element(*LoginPageLocators.REG_CONFIRM_PASSWORD_FIELD)
    confirm_password_field.send_keys(password)
    register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
    register_button.click()

    self.should_be_authorized_user()

    return email, password