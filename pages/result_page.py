from pages.base_page import BasePage
from resources.locators import SearchResultLocators

game_name="Starcraft II"

class ResultPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.enter_search_game(game_name)

    def click_channel_tab(self):
        self.click(SearchResultLocators.channel_tab)
