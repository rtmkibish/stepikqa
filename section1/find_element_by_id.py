from selenium import webdriver


URL_EXAMPLE = "http://suninjuly.github.io/cats.html"
driver = webdriver.Chrome()
driver.get(URL_EXAMPLE)
lenin_title_picture = driver.find_element_by_id("politic")
assert lenin_title_picture.text == "Lenin cat"
driver.close()
