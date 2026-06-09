import pytest
from selenium import webdriver
import read_config

@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup_and_teardown(request):
    browser = read_config.get_config("basic info", "browser")

    if request.param == "chrome":
        driver = webdriver.Chrome()

    elif request.param == "firefox":
        driver = webdriver.Firefox()

    elif request.param == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.implicitly_wait(5)
    url = read_config.get_config("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()