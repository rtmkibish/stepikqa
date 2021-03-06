import pytest


class TestClass:
  """ To test pametrized tests """

  @pytest.mark.parametrize('key,value',[(1, 2), (2, 2), (3, 2), pytest.param(4, 4, marks=pytest.mark.xfail)])
  def test_pameters(self, key, value):
    assert key != value, f'Key {key} must not be equal to value {value}'
