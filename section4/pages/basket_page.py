from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
  """
  Represents the Basket Page
  """

  def should_not_be_products(self):
    assert not self.is_element_present(*BasketPageLocators.BASKET_PRODUCTS_FORM), 'Basket holds products but it must not'

  def should_be_basket_empty_message(self):
    assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), 'Basket is empty message should be presented'
