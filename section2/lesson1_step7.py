import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
try:
    driver = webdriver.Chrome()
    driver.get(link)
    treasure_image = driver.find_element(By.XPATH, '//img[@id="treasure"]')
    x_value = treasure_image.get_attribute('valuex')
    answer = calc(x_value)
    text_field = driver.find_element(By.XPATH, '//*[@id="answer"]')
    text_field.send_keys(answer)
    checkbox = driver.find_element(By.XPATH, '//div//input[@id="robotCheckbox"]')
    checkbox.click()
    radiobutton = driver.find_element(By.XPATH, '//div//input[@id="robotsRule"]')
    radiobutton.click()
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
except Exception as e:
    print(e)
finally:
    driver.quit()
