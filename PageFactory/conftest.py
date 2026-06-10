import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup_and_teardown(request):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")

    request.cls.driver = driver

    yield

    driver.quit()