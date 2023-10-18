from base_test import BaseTest
import os
import sys

base_dir = os.path.dirname(__file__) or '.'
sys.path.append("../")

from pages.home_page import HomePage


class TestHomePage(BaseTest):
    
    def setUp(self):
        self.home_page = HomePage(self.driver)
    
    def test_search_button(self):
        self.home_page.click_search_button()


