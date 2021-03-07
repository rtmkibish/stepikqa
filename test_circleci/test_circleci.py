def test_env(session_env):
  assert session_env == 'http://somesite.domain.com'

def test_credentials(credentials):
  assert credentials.get('login') == 'login'
  assert credentials.get('password') == 'password'
