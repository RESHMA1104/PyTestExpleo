import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import read_config
from Utilities import logCreator

class HomePage:
    logger = logCreator.log_generator()
    def __init__(self, driver):
        self.driver = driver
        self.logger.info("Driver Initialized")

    home_page_link = "//span[text() = 'My Account']"
    login_info = "//span[text()='My Account']/ancestor::li//a[text()='Login']"
    login_email_id = "//input[@placeholder='E-Mail Address']"
    login_password = "//input[@id='input-password']"
    login_btn = "//input[@value='Login']"

    def home_page(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.home_page_link).click()
        self.logger.info("Home page is launched")
    def login_link(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.login_info).click()
        self.logger.info("Login Page is visible")
    def email_id(self):
        time.sleep(5)
        val = read_config.get_config("login credentials", "email")
        self.driver.find_element(By.XPATH, self.login_email_id).send_keys(val)
        self.logger.info("User enters email")
    def password_id(self):
        time.sleep(5)
        val = read_config.get_config("login credentials", "password")
        self.driver.find_element(By.XPATH, self.login_password).send_keys(val)
        self.logger.info("User enters password")
    def login_button(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.login_btn).click()
        self.logger.info("Login button is clicked")