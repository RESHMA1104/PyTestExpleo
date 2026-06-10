import pytest
from selenium.webdriver.common.by import By
import read_config

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:

    def test_validLogin(self):
        val = read_config.get_config("search term", "valid")
        self.driver.find_element(By.NAME, "search").send_keys(val)
        self.driver.find_element(By.XPATH,'//button[@class="btn btn-default btn-lg"]').click()
        assert self.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()