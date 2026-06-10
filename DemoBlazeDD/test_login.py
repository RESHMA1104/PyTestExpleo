import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@onclick="logIn()"]'))).click()
        assert WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "nameofuser"))).is_displayed()

    def test_InvalidProduct(self):
        self.driver.find_element(By.ID, "login2").click()
        user = read_config.get_config("Invalid credentials", "Inusername")
        pas = read_config.get_config("Invalid credentials", "Inpassword")
        self.driver.find_element(By.ID, "loginusername").send_keys(user)
        self.driver.find_element(By.ID, "loginpassword").send_keys(pas)
        self.driver.find_element(By.XPATH,'//button[@onclick="logIn()"]').click()
        time.sleep(5)
        alert = self.driver.switch_to.alert
        actual_result = alert.text
        expected_result = "Wrong password."
        assert actual_result == expected_result
        alert.accept()