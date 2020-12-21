from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/huge_form.html")
    text_fields_list = driver.find_elements(By.XPATH, "//form//input[@type=\"text\"]")
    submit_button = driver.find_element(By.XPATH, "//form//button[@type=\"submit\"]")
    for field in text_fields_list:
        field.send_keys("Test text")
    submit_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
except Exception as e:
    print(e)
finally:
    sleep(15)
    driver.quit()
