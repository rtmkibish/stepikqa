import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
  """ This test will raise the FAILED status in the console as we marked that
  it should fail but it is not"""
  assert True


@pytest.mark.xfail
def test_not_succeed():
  assert False


@pytest.mark.skip
def test_skipped():
  assert False
