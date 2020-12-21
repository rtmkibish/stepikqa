from time import sleep
from selenium import webdriver


try:
    driver = webdriver.Chrome()
    driver.execute_script('document.title = "Test"; alert("test")')
    sleep(10)
except Exception as e:
    print(e)
finally:
    driver.quit()