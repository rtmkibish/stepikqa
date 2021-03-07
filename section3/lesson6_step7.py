import pytest


link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.rerun_test
def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    assert True

@pytest.mark.rerun_test
def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")

@pytest.mark.flaky(reruns=3)
@pytest.mark.rerun_test
def test_example():
    import random
    assert random.choice([True, False])
