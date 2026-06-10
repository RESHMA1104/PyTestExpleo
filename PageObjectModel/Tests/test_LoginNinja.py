import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.HomePage import HomePage

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login(self):
        homepage =  HomePage(self.driver)
        homepage.home_page()
        homepage.login_link()
        homepage.email_id()
        homepage.password_id()
        homepage.login_button()