import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.SearchPage import SearchPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search(self):
        searchpage = SearchPage(self.driver)
        searchpage.search_Term_product
        searchpage.Search_button