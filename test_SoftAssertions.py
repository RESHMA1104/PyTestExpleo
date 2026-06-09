import pytest
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    yield driver
    driver.quit()

def test_validProduct(driver):
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
    
    # Soft assertions
    check.is_true(driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed(), "Product not displayed")
    check.is_in("HP", driver.title, "Title does not contain HP")

def test_invalid_product(driver):
    driver.find_element(By.NAME, "search").send_keys("Honda")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    expected_res = "There is no product that matches the search criteria."
    actual_res = driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
    check.is_true(actual_res == expected_res)

def test_no_product(driver):
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    expected_res = "There is no product that matches the search criteria."
    actual_res = driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
    check.is_true(actual_res == expected_res)