from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class MainPage(BasePage):
  """
  Represents the Main page
  """

  def go_to_login_page(self):
    login_link = self._browser.find_element(By.XPATH, '//*[@id="login_link"]')
    login_link.click()
