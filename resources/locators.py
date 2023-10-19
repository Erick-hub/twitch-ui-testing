
from selenium.webdriver.common.by import By
import pytest

game_name="Starcraft II "


class HomePageLocators():
    search_button= (By.CSS_SELECTOR,'a[href*="/search"]')

class SearchPageLocators():
    search_bar = (By.CSS_SELECTOR,'input[placeholder="Search..."]')

class SearchResultLocators():
    channel_tab = (By.XPATH,"//*[text()='Channels']")
    streamer_list=(By.CLASS_NAME,"ScCoreLink-sc-16kq0mq-0")
    scrollable_div= (By.CLASS_NAME, 'hrJbhZ ')
    window_body=(By.TAG_NAME, 'body')


class StreamLocators():
    content_warning_button= (By.XPATH,"//*[text()='Start Watching']")
    chat_room_welcome=(By.XPATH,"//*[text()='Welcome to the chat room!']")

    