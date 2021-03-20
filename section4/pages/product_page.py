from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
  """
  Represents product page
  """

  def add_product_to_basket(self):
    add_product_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
    add_product_to_basket.click()

  def should_be_added_correct_product_name(self):
    try:
      message_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_MESSAGE).text
    except NoSuchElementException:
      raise AssertionError("Correct product name should be presented in the message")

    product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    assert message_product_name == product_name, "Product name should be the same in the message"

  def should_basket_price_equal_to_product_price(self):
    product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
    basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
    assert basket_total_price.strip() == product_price

  def should_message_price_be_equal_to_product_price(self):
    product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
    try:
      message_product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_PRICE).text
    except NoSuchElementException:
      raise AssertionError("Correct product price should be presented in the message")

    assert product_price == message_product_price, "Product price should be the same in the message"

  def is_not_product_added_message(self):
    assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), 'Product message appeared but it must not'

  def is_product_message_disappeared(self):
    assert self.is_disapeared(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), 'Product message did not disappeared but must'
