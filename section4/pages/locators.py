from selenium.webdriver.common.by import By


class BasePageLocators:
  LOGIN_LINK = (By.XPATH, '//*[@id="login_link"]')


class LoginPageLocators:
  LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
  REGISTER_FORM = (By.XPATH, '//*[@id="register_form"]')


class ProductPageLocators:
  PRODUCT_PRICE = (By.XPATH, '//div[@id="content_inner"]//article//div[@class="col-sm-6 product_main"]//p')
  PRODUCT_NAME = (By.XPATH, '//div[@id="content_inner"]//article//div[@class="col-sm-6 product_main"]//h1')
  ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]//button[@type="submit"]')
  BASKET_PRICE = (By.XPATH, '//div//strong/ancestor::*[position()=1]')
  PRODUCT_ADDED_MESSAGE = (By.XPATH, '//div[@id="messages"]/div[1]/div/strong')
  PRODUCT_MESSAGE_PRICE = (By.XPATH, '//div[@id="messages"]/div[3]/div/p/strong')
