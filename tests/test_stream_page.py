from base_test import BaseTest


from pages.stream_page import StreamPage


class TestStreamPage(BaseTest):
    
    def test_stream_screenshot(self):
        self.stream_page=StreamPage(self.driver)
        try:
            self.stream_page.click_content_warning_button()
        except:
            pass
        try:
            self.stream_page.get_chat_room_welcome()
        except:
            pass
        self.stream_page.take_screenshot('streamer_screenshot.png')
          