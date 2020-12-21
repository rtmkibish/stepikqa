from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/math.html'
driver = webdriver.Chrome()
driver.get(link)
radio_btn = driver.find_element(By.XPATH, '//input[@id="peopleRule"]')
is_checked = radio_btn.get_attribute('checked')
assert is_checked is None, 'some text'
