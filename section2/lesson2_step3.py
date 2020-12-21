from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html' # different select type
try:
    driver = webdriver.Chrome()
    driver.get(link)
    first_digit = driver.find_element(By.XPATH, '//form//span[2]').text
    second_digit = driver.find_element(By.XPATH, '//form//span[4]').text
    elements_sum = int(first_digit) + int(second_digit)
    select = Select(driver.find_element(By.XPATH, '//form//div/label//following::select'))
    select.select_by_visible_text(str(elements_sum))
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_button.click()
    alert = driver.switch_to.alert
    print(alert.text)
except Exception as e:
    print(e)
finally:
    driver.quit()

