from pages.base_page import BasePage
from resources.locators import HomePageLocators


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.twitch.tv/")

    def click_search_button(self):
        self.click(HomePageLocators.search_button)
