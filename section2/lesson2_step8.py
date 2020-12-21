from os import path
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/file_input.html'
try:
    driver = Chrome()
    driver.get(link)
    first_name = driver.find_element(By.XPATH, '//form//input[@name="firstname"]')
    first_name.send_keys('artem')
    last_name = driver.find_element(By.XPATH, '//form//input[@name="lastname"]')
    last_name.send_keys('test')
    email = driver.find_element(By.XPATH, '//form//input[@name="email"]')
    email.send_keys('test@test.com')
    file = driver.find_element(By.XPATH, '//form//input[@type="file"]')
    current_dir = path.abspath(path.dirname(__file__))
    file.send_keys(path.join(current_dir, 'test.txt'))
    submit_button = driver.find_element(By.XPATH, '//form//button[@type="submit"]')
    submit_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
except Exception as e:
    print(e)
finally:
    driver.quit()
