import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/math.html'
    driver = webdriver.Chrome()
    driver.get(link)
    x_value = driver.find_element(By.XPATH, '//label//span[2]')
    x_result = calc(x_value.text)
    text_field = driver.find_element(By.XPATH, '//input[@id="answer"]')
    text_field.send_keys(x_result)
    robot_checkbox = driver.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    robot_checkbox.click()
    robot_radio = driver.find_element(By.XPATH, '//input[@id="robotsRule"]')
    robot_radio.click()
    submit_button = driver.find_element(By.XPATH, '//button')
    submit_button.click()
    alert = driver.switch_to.alert
    answer = alert.text[-18:]
    print(answer)
    alert.accept()
except Exception as e:
    print(e)
    sleep(5)
finally:
    driver.quit()
