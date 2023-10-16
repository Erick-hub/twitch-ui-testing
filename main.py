from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import time


game_name='League of Legends'
url_search_game_name=game_name.replace(" ","+")

mobile_emulation = {
    "deviceMetrics": { "width": 412, "height": 915, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19" }


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver=webdriver.Chrome(chrome_options)
driver.get("https://www.twitch.tv/")
driver.implicitly_wait(3)
try:
  search_button= driver.find_element(By.CSS_SELECTOR,'a[href*="/search"]')
except:
  print('search button not found')
search_button.click()
try:
  search_bar= driver.find_element(By.CSS_SELECTOR,'input[placeholder="Search..."]')
except:
  print('search bar not found')


search_bar.clear()
search_bar.send_keys(game_name)
search_bar.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR,f'a[href*="/search?term={url_search_game_name}&type=channels"]').click()


#true page scrollbar
body= driver.find_element(By.TAG_NAME, 'body')
#scrollable div
div_scroll= driver.find_element(By.CLASS_NAME, 'hrJbhZ ')


body.send_keys(Keys.ARROW_DOWN)
driver.execute_script("arguments[0].scroll({top: arguments[0].scrollHeight, behavior: 'smooth'})", div_scroll)
time.sleep(1)
driver.execute_script("arguments[0].scroll({top: arguments[0].scrollHeight, behavior: 'smooth'})", div_scroll)


