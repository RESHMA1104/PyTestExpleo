import pytest

@pytest.mark.order(2)
def test_login():
    print("Login executed")

@pytest.mark.order(3)
def test_dashboard():
    print("Dashboard executed")

@pytest.mark.order(1)
def test_logout():
    print("Logout executed")