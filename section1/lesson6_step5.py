import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


URL = "http://suninjuly.github.io/find_link_text"
driver = webdriver.Chrome()
driver.get(URL)
link = driver.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()
first_name = driver.find_element(By.XPATH, "//form//div[1]//input")
last_name = driver.find_element(By.XPATH, "//form//div[2]//input")
city = driver.find_element(By.XPATH, "//form//div[3]//input")
country = driver.find_element(By.XPATH, "//form//div[4]//input")
submit_button = driver.find_element(By.XPATH, "//form//button")

first_name.send_keys("Ivan")
last_name.send_keys("Petrov")
city.send_keys("Smolensk")
country.send_keys("Russia")
submit_button.click()

alert = Alert(driver)
print(alert.text)
sleep(30)
driver.quit()
