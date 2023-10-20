from pages.channel_result_page import ChannelResultsPage
from resources.locators import StreamLocators


class StreamPage(ChannelResultsPage):
    def __init__(self, driver, *streamer):
        super().__init__(driver)
        if streamer:
            self.driver.get(f"https://www.twitch.tv/{streamer}")
        else:
            self.scroll_down()
            self.scroll_down()
            streamer_element = self.get_random_streamer()
            streamer_element.click()

    def click_content_warning_button(self):
        self.click(StreamLocators.content_warning_button)

    def get_chat_room_welcome_element(self):
        self.get_single_element(StreamLocators.chat_room_welcome)
