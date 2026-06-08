import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")
    yield driver
    driver.quit()
def test_valid_product(driver):
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    assert driver.find_element(By.XPATH,"//*[text()='HP LP3065']").is_displayed()
def test_invalid_product(driver):
    driver.find_element(By.NAME, "search").send_keys("Honda")
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    expected_res = "There is no product that matches the search criteria."
    actual_res = driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
    assert actual_res == expected_res
def test_no_product(driver):
    driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
    expected_res = "There is no product that matches the search criteria."
    actual_res = driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
    assert actual_res == expected_res