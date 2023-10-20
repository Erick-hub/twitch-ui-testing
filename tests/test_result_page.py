from base_test import BaseTest
from pages.result_page import ResultPage


class TestResultPage(BaseTest):

    def test_click_channel_tab(self):
        self.result_page = ResultPage(self.driver)
        self.result_page.click_channel_tab()
        url_search_game_name = self.game_name.replace(" ", "+")
