from selenium import webdriver


URL_EXAMPLE = "http://python.org"
driver = webdriver.Chrome()
start_survey = driver.find_element_by_partial_link_text("Socialize")
assert start_survey.text == "Socialize"
driver.quit()
