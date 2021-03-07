import os

import pytest
from selenium import webdriver


def pytest_addoption(parser):
  parser.addoption('--env', action='store', default='Trex', help='The environment to run tests on')

# @pytest.fixture(scope="function")
# def browser():
#   browser = webdriver.Chrome()
#   browser.implicitly_wait(5)
#   yield browser
#   browser.quit()

@pytest.fixture(scope="session")
def session_env(request):
  env_key = request.config.getoption('env')
  session_env = os.environ.get(env_key)

  if session_env is None:
    raise ValueError('The env is invalid or not set')

  yield session_env

@pytest.fixture(scope="session")
def credentials():
  login = os.environ.get('OKTA_LOGIN')
  password = os.environ.get('OKTA_PASSWORD')

  if login is None:
    raise ValueError('The env login is missed')
  elif password is None:
    raise ValueError('The env password is missed')
  
  credentials = {
    'login': login,
    'password': password
  }

  yield credentials
