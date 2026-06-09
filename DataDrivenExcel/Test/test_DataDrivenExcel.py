import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from Utilities import logCreator

@pytest.mark.parametrize("username, password", excelReader.get_data(r"D:\\PyTestExpleo\\DataDrivenExcel\\ExcelFiles\\loginData.xlsx", "Sheet1"))

class TestLogin1:
    logger = logCreator.log_generator()
    def test_validation(self, username, password):
        self.logger.info("Program Execution Started")
        self.driver = webdriver.Chrome()
        self.logger.info("WebDriver Started")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.logger.info("Wait Implemented")
        self.driver.get("https://demoblaze.com/")
        self.logger.info("DemoBlaze Application is launched")
        self.driver.find_element(By.ID, "login2").click()
        self.logger.info("User clicks login")
        self.driver.find_element(By.ID, "loginusername").send_keys(username)
        self.logger.info("UserName is entered")
        self.driver.find_element(By.ID, "loginpassword").send_keys(password)
        self.logger.info("Password is entered")
        self.driver.find_element(By.XPATH,'//button[@onclick="logIn()"]').click()
        self.logger.info("User clicks on login button")
        self.driver.quit()