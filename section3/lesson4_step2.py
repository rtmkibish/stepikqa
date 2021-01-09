from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestTitle1:
  """In this class we are using classmethod based fixtures.
  They will be run one before all test execution and one after all tests execution.
  """

  link = 'http://selenium1py.pythonanywhere.com/'

  @classmethod
  def setup_class(cls):
    """It will be run before all tests"""

    print('Preparing browser...')
    cls.browser = webdriver.Chrome()
  
  @classmethod
  def teardown_class(cls):
    """It will be run after all tests"""

    print('Closing browser...')
    cls.browser.quit()
  
  def test_title_should_be_Oscar_Sandbox(self):
    self.browser.get(self.link)
    title = self.browser.title
    assert title  == 'Oscar - Sandbox', 'Page title should be equal to "Oscar - Sandbox"'

  def test_new_tab_title_All_products_Oscar_Sandbox(self):
    self.browser.get(self.link)
    self.browser.find_element(By.XPATH, '//a[text() = "All products"]').send_keys(Keys.COMMAND, Keys.ENTER)
    new_tab = self.browser.window_handles[1]
    self.browser.switch_to.window(new_tab)
    title = self.browser.title
    assert title == 'All products | Oscar - Sandbox', 'Page title should be equal to "All products | Oscar - Sandbox"'


class TestTitle2:
  """In this class we are using fixtures for each test.
  They will be run one before a test and one after the tests.
  """

  link = 'http://selenium1py.pythonanywhere.com/'

  def setup_method(self):
    """Will be run before each test"""

    print('Preparing browser for a test...')
    self.browser = webdriver.Chrome()

  def teardown_method(self):
    """Will be run after each test"""

    print('Closing browser after the test...')
    self.browser.quit()

  def test_title_should_be_Oscar_Sandbox(self):
    self.browser.get(self.link)
    title = self.browser.title
    assert title  == 'Oscar - Sandbox', 'Page title should be equal to "Oscar - Sandbox"'

  def test_new_tab_title_All_products_Oscar_Sandbox(self):
    self.browser.get(self.link)
    self.browser.find_element(By.XPATH, '//a[text() = "All products"]').send_keys(Keys.COMMAND, Keys.ENTER)
    new_tab = self.browser.window_handles[1]
    self.browser.switch_to.window(new_tab)
    title = self.browser.title
    assert title == 'All products | Oscar - Sandbox', 'Page title should be equal to "All products | Oscar - Sandbox"'
