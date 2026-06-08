import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By 

@pytest.mark.parametrize("search_term",[('selenium'),('Pytest'),('Selenium locators')])
def test_google_search(search_term):
    driver=webdriver.Chrome()
    driver.maximize_window
    driver.get("https://www.google.co.in/")
    driver.find_element(By.NAME,"q").send_keys(search_term)
    time.sleep(5)
    driver.find_element(By.CLASS_NAME,"gNO89b").click()