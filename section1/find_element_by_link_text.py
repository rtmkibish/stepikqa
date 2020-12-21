from selenium import webdriver


URL_EXAMPLE = "http://python.org"
driver = webdriver.Chrome()
driver.get(URL_EXAMPLE)
start_survey = driver.find_element_by_link_text("Start the survey!")
assert start_survey.text == "Start the survey!"
driver.quit()
