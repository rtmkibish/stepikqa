from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


URL_EXAMPLE = "http://suninjuly.github.io/simple_form_find_task.html"
driver = webdriver.Chrome()
driver.get(URL_EXAMPLE)
first_name_field = driver.find_element(By.XPATH, "//input[@name=\"first_name\"]")
last_name_field = driver.find_element(By.XPATH, "//input[@name=\"last_name\"]")
city_field = driver.find_element(By.XPATH, "//label[contains(text(), \"City:*\")]//following::input")
country_field = driver.find_element(By.XPATH, "//input[@id=\"country\"]")
submit_button = driver.find_element(By.XPATH, "//form//button")

first_name_field.send_keys("Ivan")
last_name_field.send_keys("Petrov")
city_field.send_keys("Smolensk")
country_field.send_keys("Russia")
submit_button.click()

sleep(30)
driver.quit()
