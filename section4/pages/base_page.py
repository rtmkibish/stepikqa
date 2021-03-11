class BasePage:
  """
  Some kind of interface for future page object classes
  """

  def __init__(self, url, browser):
    self._url = url
    self._browser = browser

  def open(self):
    self._browser.get(self._url)
