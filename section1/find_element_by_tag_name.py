from selenium import webdriver


URL_EXAMPLE = "http://suninjuly.github.io/cats.html"
driver = webdriver.Chrome()
driver.get(URL_EXAMPLE)
h1 = driver.find_element_by_tag_name("h1")
assert h1.text == "Cat memes"
driver.quit()
