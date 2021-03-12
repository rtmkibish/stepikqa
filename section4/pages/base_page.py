from selenium.common.exceptions import NoSuchElementException


class BasePage:
  """
  Some kind of interface for future page object classes
  """

  def __init__(self, url, browser, timeout=10):
    self.url = url
    self.browser = browser
    self.browser.implicitly_wait(timeout)

  def open(self):
    self.browser.get(self.url)

  def is_element_present(self, how, what):
    try:
      self.browser.find_element(how, what)
    except NoSuchElementException:
      return False
    return True
