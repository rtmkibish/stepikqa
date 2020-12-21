from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/cats.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.XPATH, '//*[@id="button"]')
    print(button.text)
except Exception as e:
    print(type(e))
finally:
    browser.quit()
