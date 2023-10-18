from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from random import choice
import time
import pytest

@pytest.mark.usefixtures("get_driver","get_game_name")
class TestSearchButton():
  
    def test_search_bar(self):
        driver=self.driver
        driver.find_element(By.CSS_SELECTOR,'a[href*="/search"]').click()
        
        search_bar= driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search..."]')
        search_bar.clear()
        search_bar.send_keys(self.game_name)
        search_bar.send_keys(Keys.ENTER)


        #click on channels tab
        driver.find_element(By.CSS_SELECTOR,f'a[href*="/search?term={self.game_name.replace(" ","+")}&type=channels"]').click()


        
        #scrollable div
        div_scroll= driver.find_element(By.CLASS_NAME, 'hrJbhZ ')

        #window page scrollbar
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
        
        
        #scroll twice
        driver.execute_script("arguments[0].scroll({top: arguments[0].scrollHeight, behavior: 'smooth'})", div_scroll)
        time.sleep(1)
        driver.execute_script("arguments[0].scroll({top: arguments[0].scrollHeight, behavior: 'smooth'})", div_scroll)
        time.sleep(1)

        #find all streamer elements, it might contain streamers that just finished streaming
        streamer_list= driver.find_elements(By.CLASS_NAME,"ScCoreLink-sc-16kq0mq-0")

        #choose random streamer
        streamer= choice(streamer_list)
        streamer_url= streamer.get_attribute('href')
        streamer.click()


        sleep_time=5
        try:
        #some streams provide content warning and requires the press of a button to watch
            content_warning_button= driver.find_element(By.XPATH,"//*[text()='Start Watching']")
            content_warning_button.click()
        except:
        #if the button is not found ,implicit await already waited for 5 seconds
            sleep_time=0

        #if the streamer is not live, we should have been redirected to their homepage by now
        if driver.current_url != streamer_url:
            driver.save_screenshot('streamer_screenshot_homepage.png')
            input()

        WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH,"//*[text()='Welcome to the chat room!']")),'Video loaded' 
        )

        #wait for buffer, if there was no content warning, we already waited enough
        time.sleep(sleep_time)

        driver.save_screenshot('streamer_screenshot.png')
        