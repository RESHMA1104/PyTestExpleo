import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.mark.parametrize('input_browser', ['chrome', 'firefox'])
@pytest.mark.parametrize('input_url', ['https://www.flipkart.com', 'https://www.amazon.com'])
def test_url_on_browser(input_browser, input_url):

    if input_browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--headless")   
        web_driver = webdriver.Chrome(options=options)

    elif input_browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--headless")   
        web_driver = webdriver.Firefox(options=options)

    web_driver.maximize_window()
    web_driver.get(input_url)

    print(web_driver.title)

    time.sleep(2)
    web_driver.quit()