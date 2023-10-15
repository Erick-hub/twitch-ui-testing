from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19" }


chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver=webdriver.Chrome(chrome_options)
driver.get("https://www.twitch.tv/")
driver.implicitly_wait(8)
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
search_bar.send_keys("StarCraft II")
search_bar.send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR,'a[href*="/search?term=StarCraft+II&type=channels"]').click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(10)

