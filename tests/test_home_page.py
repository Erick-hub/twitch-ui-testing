from base_test import BaseTest
import os
import sys


from pages.home_page import HomePage


class TestHomePage(BaseTest):

    def test_search_button(self):
        self.home_page = HomePage(self.driver)
        self.home_page.click_search_button()
