from selenium.common.exceptions import NoAlertPresentException

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
  """
  Represents product page
  """

  def add_product_to_basket(self):
    add_product_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
    add_product_to_basket.click()

  def should_be_product_addition_massage_alert(self):
    try:
      self.browser.switch_to.alert
    except NoAlertPresentException:
      raise AssertionError("Product added to the basket alert message should be presented")

  def should_basket_price_equal_to_product_price(self):
    product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
    basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
    assert basket_total_price.strip() == product_price
