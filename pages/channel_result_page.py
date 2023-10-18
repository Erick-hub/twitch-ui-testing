from random import choice
from typing import KeysView
from pages.base_page import BasePage
from resources.locators import SearchResultLocators
from resources.scripts import SearchResultScripts


class ChannelResultsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.click(SearchResultLocators.channel_tab)
    
    def get_visible_streamers(self):        
        streamer_list= self.get_multiple_elements(SearchResultLocators.streamer_list)
        return streamer_list
    
    def scroll_down(self):
      
        div_scroll= self.get_single_element(SearchResultLocators.scrollable_div)        
        self.enter_text(SearchResultLocators.window_body,KeysView.PAGE_DOWN)
        self.execute_script(SearchResultScripts.scroll_down_element,div_scroll)

        
    def click_streamer_name(self,streamer):
        #choose random streamer
        streamer.click()
    def click_random_streamer_name(self,streamer):
        #choose random streamer
        streamer=choice(self.get_visible_streamers())
        streamer.click()