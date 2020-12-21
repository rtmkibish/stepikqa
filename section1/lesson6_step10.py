from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome()
    driver.get(link)
    required_fields = driver.find_elements(By.XPATH, "//form//div//div//label//following::input[@required]")
    for field in required_fields:
        field.send_keys("Text")
    submit_button = driver.find_element(By.XPATH, "//form//button[@type=\"submit\"]")
    submit_button.click()
    sleep(3)
    welcome_text_element = driver.find_element(By.XPATH, "/html//body//h1")
    assert welcome_text_element.text == "Congratulations! You have successfully registered!"
except Exception as e:
    print(e)
finally:
    sleep(5)
    driver.quit()
