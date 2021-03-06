import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TestParametrize:
  """
  Tests different telinks in one test
  """

  @pytest.mark.parametrize('url', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
  def test_optional_field_returns_correct(self, browser, url):
    browser.get(url)
    unsver_field = browser.find_element(By.XPATH, '//textarea[contains(@placeholder, "Type your answer here...")]')
    unsver_field.send_keys(str(math.log(int(time.time()))))
    submit_button = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
    submit_button.click()
    result_field = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//pre[@class="smart-hints__hint"]')))
    assert result_field.text == "Correct!", f"{result_field.text}"
