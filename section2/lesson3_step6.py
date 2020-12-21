from math import log, sin
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc_x(x):
    return log(abs(12*sin(x)))

link = 'http://suninjuly.github.io/redirect_accept.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '//form//button')
    button.click()
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
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
