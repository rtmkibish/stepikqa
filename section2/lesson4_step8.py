from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc_x(x: int):
    return log(abs(12*sin(x)))


link = 'http://suninjuly.github.io/explicit_wait2.html'
try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), '$100'))
    button = browser.find_element(By.XPATH, '//*[@id="book"]')
    button.click()
    x_value = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
    answer = calc_x(int(x_value))
    answer_field = browser.find_element(By.XPATH, '//form//input[@type="text"]')
    answer_field.send_keys(str(answer))
    submit_button = browser.find_element(By.XPATH, '//form//button')
    submit_button.click()
    alert_text = browser.switch_to.alert.text
    print(alert_text.split(':')[1])
except Exception as e:
    print(e)
finally:
    browser.quit()
