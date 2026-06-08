import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_validProduct(self):
        self.find_element(By.NAME, "search").send_keys("HP")
        self.find_element(By.XPATH, '//button[@class="btn btn-default btn-lg"]').click()
        assert self.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    def test_invalidProduct(self):
        self.find_element(By.NAME, "search").send_keys("Honda")
        self.find_element(By.XPATH, '//button[@class="btn btn-default btn-lg"]').click()
        expected_text = "There is no product that matches the search criteria."
        assert self.find_element(By.XPATH, "//input[@id='button-search']//following-sibling::p").text.__eq__(expected_text)