import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def scroll_and_click(element):
    driver.execute_script('return arguments[0].scrollIntoView(true)', element)
    element.click()


link = 'http://suninjuly.github.io/execute_script.html'
try:
    driver = webdriver.Chrome()
    driver.get(link)
    x_value = driver.find_element(By.XPATH, '//*[@id="input_value"]').text
    answer = math.log((abs(12 * math.sin(int(x_value)))))
    text_field = driver.find_element(By.XPATH, '//form//input[@type="text"]')
    text_field.send_keys(str(answer))
    checkbox = driver.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    checkbox.click()
    radio_button = driver.find_element(By.XPATH, '//*[@id="robotsRule"]')
    scroll_and_click(radio_button)
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    scroll_and_click(submit_button)
    alert = driver.switch_to.alert
    print(alert.text)
except Exception as e:
    print(e)
finally:
    driver.quit()

