import pytest
from chromedriver_py import binary_path as chrome_path
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
  browser = Chrome(executable_path=chrome_path)
  browser.implicitly_wait(5)
  yield browser
  browser.quit()

class TestShadowDOM:
  """Suite for tests related to Shadow DOM technology"""
  DEFAULT_SITE_LINK = 'https://www.alodokter.com/'

  def test_kari_dokter_page_should_open(self, browser):
    browser.get(self.DEFAULT_SITE_LINK)
    shadow_host = browser.find_element(By.XPATH, '//hero-view')
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', shadow_host)
    cari_dokter_btn = shadow_root.find_element(By.CSS_SELECTOR, 'a[href="/cari-dokter"]')
    cari_dokter_btn.click()
    assert browser.title == 'Cari Dokter Spesialis sesuai Kebutuhan Anda'
