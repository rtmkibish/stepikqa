import pytest


@pytest.mark.citest
def test_hello_natasha():
  assert 'Natasha' == 'Natasha'

def test_hello_artem():
  assert 'Artem' == 'Artem'
