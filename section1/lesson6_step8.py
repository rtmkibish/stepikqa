from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/find_xpath_form")
    submit_button = driver.find_element(By.XPATH, "//form//button[contains(text(), \"Submit\") and @type=\"submit\"]")
    inputs = driver.find_elements(By.XPATH, "//form//div//input")
    for field in inputs:
        field.send_keys("Test")
    submit_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
finally:
    sleep(10)
    driver.quit()
