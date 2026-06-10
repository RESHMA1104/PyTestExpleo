import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:

    def test_validProduct(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        self.driver.find_element(By.XPATH,'//button[@class="btn btn-default btn-lg"]').click()
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    def test_invalidProduct(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH,'//button[@class="btn btn-default btn-lg"]').click()
        expected_text = "There is no product that matches the search criteria."
        actual_text = self.driver.find_element(By.XPATH,"//input[@id='button-search']//following-sibling::p").text
        assert actual_text == expected_text

    def test_no_product(self):
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        expected_res = "There is no product that matches the search criteria."
        actual_res = self.driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
        assert actual_res == expected_res