import pytest

@pytest.mark.dependency(name="login")
def test_login():
    assert True

@pytest.mark.dependency(depends=["login"])
def test_dashboard():
    assert True

@pytest.mark.dependency(depends=["login"])
def test_logout():
    assert True