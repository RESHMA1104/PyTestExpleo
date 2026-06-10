import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import read_config


@pytest.mark.usefixtures("setup_and_teardown")
class TestLoginRelative:

    def test_valid_login(self):
        self.driver.find_element(By.ID, "login2").click()
        username = read_config.get_config("login credentials", "username")
        password = read_config.get_config("login credentials", "password")
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "loginpassword")))
        username_field = self.driver.find_element(locate_with(By.TAG_NAME, "input").above(password_field))
        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button = self.driver.find_element(locate_with(By.XPATH, '//button[@onclick="logIn()"]').below(password_field))
        login_button.click()
        welcome_user = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        assert welcome_user.is_displayed()
        print("Login Successful")
        print("User:", welcome_user.text)