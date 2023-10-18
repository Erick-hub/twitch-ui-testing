from pages.base_page import BasePage
from resources.locators import StreamLocators


class StreamPage(BasePage):
    def __init__(self, driver,streamer):
        super().__init__(driver)
        self.click_streamer_name(streamer)
    
    def click_content_warning_button(self):
        self.click(StreamLocators.content_warning_button)