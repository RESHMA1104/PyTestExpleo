import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from Utilities import logCreator

@pytest.mark.parametrize("email, password", excelReader.get_data(r"D:\\PyTestExpleo\\TutorialsNinja\\ExcelFiles\\NinjaloginData.xlsx", "Sheet1"))

class TestLogin1:
    logger = logCreator.log_generator()
    def test_validation(self, email, password):
        self.logger.info("Program Execution Started")
        self.driver = webdriver.Chrome()
        self.logger.info("WebDriver Started")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.logger.info("Wait Implemented")
        self.driver.get("https://tutorialsninja.com/demo/")
        self.logger.info("Tutorials Ninja is launched")
        self.driver.find_element(By.XPATH, "//span[text() = 'My Account']").click()
        self.logger.info("User clicks Account")
        self.driver.find_element(By.XPATH, "//span[text()='My Account']/ancestor::li//a[text()='Login']").click()
        self.logger.info("User clicks login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='E-Mail Address']").send_keys(email)
        self.logger.info("UserName is entered")
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys(password)
        self.logger.info("Password is entered")
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        self.logger.info("User clicks on login button")
        self.driver.quit()