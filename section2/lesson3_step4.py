import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc_x(x):
    return math.log(abs(12 * math.sin(x)))

link = 'http://suninjuly.github.io/alert_accept.html'
try:
    driver = webdriver.Chrome()
    driver.get(link)
    button = driver.find_element(By.XPATH, '//form//button')
    button.click()
    alert = driver.switch_to.alert
    alert.accept()
    x_value = driver.find_element(By.XPATH, '//*[@id="input_value"]').text
    answer = calc_x(int(x_value))
    answer_field = driver.find_element(By.XPATH, '//form//input[@id="answer"]')
    answer_field.send_keys(str(answer))
    submit_button = driver.find_element(By.XPATH, '//form//button')
    submit_button.click()
    result_text = driver.switch_to.alert.text
    print(result_text)
    final_result = result_text.split(':')[1]
    print(final_result)
except Exception as e:
    print(e)
finally:
    driver.quit()
