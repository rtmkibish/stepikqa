from time import sleep
from selenium import webdriver


URL_EXAMPLE = "http://suninjuly.github.io/xpath_examples"
driver = webdriver.Chrome()
driver.get(URL_EXAMPLE)
gold_button = driver.find_element_by_css_selector("div:nth-child(2)>button:nth-child(3)")
gold_button.click()
sleep(3)
driver.close()
