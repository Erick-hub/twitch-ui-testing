from pages.search_page import SearchPage
from resources.locators import SearchResultLocators
import time
game_name="Starcraft II"

class ResultPage(SearchPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.enter_search_game(game_name)

    def click_channel_tab(self):
        self.click(SearchResultLocators.channel_tab)
        time.sleep(3)