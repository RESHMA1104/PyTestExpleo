import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import read_config
from Utilities import logCreator

class SearchPage:
    logger = logCreator.log_generator()
    def __init__(self, driver):
        self.driver = driver
        self.logger.info("Driver Initialized")

    search_box = "//input[@name='search']"
    search_btn = "//button[@class='btn btn-default btn-lg']"
    text_match = "HP LP3065"

    def search_Term_product(self):
        time.sleep(5)
        val = read_config.get_config("Search Term", "product1")
        self.driver.find_element(By.XPATH, self.search_box).send_keys(val)
        self.logger.info("User searched for a product")
        actual_text = self.driver.find_element(By.LINK_TEXT, self.text_match).text
        expected_text = read_config.get_config("Search Term", "Text1")
        assert actual_text == expected_text,"Assertion Failed"
        self.logger.info("Assertion successful")

    def Search_button(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.search_btn).click()
        self.logger.info("User Clicks the button")