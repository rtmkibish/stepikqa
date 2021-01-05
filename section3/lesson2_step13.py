import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestRegistration(unittest.TestCase):

  REG_LINK1 = 'http://suninjuly.github.io/registration1.html'
  REG_LINK2 = 'http://suninjuly.github.io/registration2.html'

  def test_positive_registration_with_required_fields(self):
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(self.REG_LINK1)
    first_name_field = browser.find_element(By.XPATH, "//form//label[contains(text(), 'First name*')]//following::input[1]")
    first_name_field.send_keys('Artem')
    last_name_field = browser.find_element(By.XPATH, "//form//label[contains(text(), 'Last name*')]//following::input[1]")
    last_name_field.send_keys('Kibish')
    email_field = browser.find_element(By.XPATH, "//form//label[contains(text(), 'Email*')]//following::input[1]")
    email_field.send_keys('testemail@test.com')
    submit_button = browser.find_element(By.XPATH, "//form//button[@type='submit']")
    submit_button.click()
    confirmation_header = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='container']//h1"), 'Congratulations! You have successfully registered!'))
    # confirmation_text = confirmation_header.text
    # self.assertEqual(confirmation_text, 'Congratulations! You have successfully registered!', 'Failed to register a user with required fields only')
    self.assertIsNotNone(confirmation_header)
    browser.quit()

  def test_negative_registration_with_required_fields(self):
    """This method should fail with NoSuchElementException
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(self.REG_LINK2)
    first_name_field = browser.find_element(By.XPATH, "//form//label[contains(text(), 'First name*')]//following::input[1]")
    first_name_field.send_keys('Artem')
    last_name_field = browser.find_element(By.XPATH, "//form//label[contains(text(), 'Last name*')]//following::input[1]")
    last_name_field.send_keys('Kibish')
    email_field = browser.find_element(By.XPATH, "//form//label[contains(text(), 'Email*')]//following::input[1]")
    email_field.send_keys('testemail@test.com')
    submit_button = browser.find_element(By.XPATH, "//form//button[@type='submit']")
    submit_button.click()
    confirmation_header = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='container']//h1"), 'Congratulations! You have successfully registered!'))
    # confirmation_text = confirmation_header.text
    # self.assertEqual(confirmation_text, 'Congratulations! You have successfully registered!', 'Failed to register a user with required fields only')
    self.assertIsNotNone(confirmation_header)
    browser.quit()


if __name__ == "__main__":
  unittest.main()
