from base_test import BaseTest
import time

from pages.stream_page import StreamPage


class TestStreamPage(BaseTest):
    
    def test_stream_screenshot(self):
        self.stream_page=StreamPage(self.driver)
        sleep_time=3 #sleep time in case there's a content warning
        try:
            self.stream_page.click_content_warning_button()
        except:
            #if no content warning was found then browser already waited 
            sleep_time=0
            pass
        try:
            self.stream_page.get_chat_room_welcome()
        except:
            pass
        
        time.sleep(sleep_time)
        self.stream_page.take_screenshot('streamer_screenshot.png')
          