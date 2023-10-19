import pytest
from selenium import webdriver
import sys

game_name="Starcraft II "

@pytest.fixture
def get_game_name(request):
    request.cls.game_name=game_name
    return request.cls.game_name

@pytest.fixture
def get_driver(request):
   
    mobile_emulation = {
    "deviceMetrics": { "width": 412, "height": 915, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile Safari/535.19" }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    _driver=webdriver.Chrome(chrome_options)
    _driver.implicitly_wait(5)
    _driver.set_page_load_timeout(40)
    request.cls.driver=_driver
    yield request.cls.driver
    _driver.quit()