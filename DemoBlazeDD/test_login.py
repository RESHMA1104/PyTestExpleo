import pytest
from selenium.webdriver.common.by import By
import read_config
import time

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_validProduct(self):
        self.driver.find_element(By.ID, "login2").click()
        user = read_config.get_config("login credentials", "username")
        pas = read_config.get_config("login credentials", "password")
        self.driver.find_element(By.ID, "loginusername").send_keys(user)
        self.driver.find_element(By.ID, "loginpassword").send_keys(pas)
        time.sleep(10)
        self.driver.find_element(By.XPATH,'//button[@onclick="logIn()"]').click()
        assert self.driver.find_element(By.XPATH, '//a[@id="nameofuser"]').is_displayed()
    def test_InvalidProduct(self):
        self.driver.find_element(By.ID, "login2").click()
        user = read_config.get_config("Invalid credentials", "Inusername")
        pas = read_config.get_config("Invalid credentials", "Inpassword")
        self.driver.find_element(By.ID, "loginusername").send_keys(user)
        self.driver.find_element(By.ID, "loginpassword").send_keys(pas)
        self.driver.find_element(By.XPATH,'//button[@onclick="logIn()"]').click()
        time.sleep(5)
        alert = self.driver.switch_to.alert()
        actual_result = alert.text
        expected_result = "Wrong password."
        assert actual_result == expected_result
        alert.accept()