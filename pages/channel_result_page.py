from random import choice
from selenium.webdriver.common.keys import Keys
from pages.result_page import ResultPage
from resources.locators import SearchResultLocators
from resources.scripts import SearchResultScripts
from selenium.webdriver.common.by import By

import time

class ChannelResultsPage(ResultPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.click_channel_tab()
    
    def get_visible_streamers(self):       
        streamer_list= self.get_multiple_elements(SearchResultLocators.streamer_list)
        return streamer_list
    
    def get_random_streamer(self):
        streamer=choice(self.get_visible_streamers())
        return streamer
    def scroll_down(self):     
        self.get_single_element(SearchResultLocators.window_body).send_keys(Keys.PAGE_DOWN)
        div_scroll= self.get_single_element(SearchResultLocators.scrollable_div)  
        self.driver.execute_script(SearchResultScripts.scroll_down_element, div_scroll)
        time.sleep(1)

        
    