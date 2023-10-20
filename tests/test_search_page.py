from base_test import BaseTest
from pages.search_page import SearchPage


class TestSearchPage(BaseTest):

    def test_enter_game_text(self):
        self.search_page = SearchPage(self.driver)
        self.search_page.enter_search_game(self.game_name)
