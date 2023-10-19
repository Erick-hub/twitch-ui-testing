from base_test import BaseTest
from pages.channel_result_page import ChannelResultsPage
import time
import pytest
class TestChannelResultPage(BaseTest):
    
    def test_get_visible_streamers(self):
        self.channel_result_page=ChannelResultsPage(self.driver)
        streamer_list=self.channel_result_page.get_visible_streamers()
        return streamer_list

    # @pytest.mark.xfail
    def test_scroll_down(self):
        self.channel_result_page=ChannelResultsPage(self.driver)
        self.channel_result_page.scroll_down()
        time.sleep(4)
        return
    
    def test_click_random_streamer(self):
        self.channel_result_page=ChannelResultsPage(self.driver)
        streamer=self.channel_result_page.get_random_streamer()
        streamer.click()
        time.sleep(4)
