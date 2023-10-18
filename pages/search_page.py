from pages.base_page import BasePage
from resources.locators import SearchPageLocators
from selenium.webdriver.common.keys import Keys



class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.click_search_button()
    
    def enter_search_game(self,game_name):
        self.clear_text(SearchPageLocators.search_bar)
        self.enter_text(SearchPageLocators.search_bar,game_name) 
        self.enter_text(SearchPageLocators.search_bar,Keys.ENTER)







    