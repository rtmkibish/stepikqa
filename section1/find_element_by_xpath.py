from selenium import webdriver


URL_EXAMPLE = "https://github.com/rtmkibish"
driver = webdriver.Chrome()
driver.get(URL_EXAMPLE)
account_name = driver.find_element_by_xpath("//span[@class=\"p-nickname vcard-username d-block\"]")
assert account_name.text == "rtmkibish"
driver.quit()
