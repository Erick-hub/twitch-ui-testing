# Twitch UI Testing Suite 
 - Test UI navigation
 - Search bar and stream search feature
 - Screenshot ongoing stream or streamer's homepage
 

# How to run the project? 
 - Clone github repository in your local system  `git clone https://github.com/Erick-hub/twitch-ui-testing`
 - Move in twitch-ui-testing repository  `cd twitch-ui-testing`
 - Create new virtual python environment  `python3 -m venv venv`
 - Activate virtual python environment  `source venv/bin/activate` for linux, `venv\Scripts\activate.bat` for windows
 - Install all the libraries mentioned in [requirements.txt](https://github.com/Erick-hub/twitch-ui-testing/requirements.txt) using  `pip install -r requirements.txt`
 - Run Python file  `python run.py`
 
# Directory Tree
```bash
twitch-ui-testing/
┃ ┗ README.md
┣ drivers/
┣ gif/
┃ ┣ test_run.gif
┣ pages/
┃ ┣ base_page.py
┃ ┣ channel_result_page.py
┃ ┣ home_page.py
┃ ┣ result_page.py
┃ ┣ search_page.py
┃ ┣ stream_page.py
┃ ┗ __init__.py
┣ resources/
┃ ┣ locators.py
┃ ┗ scripts.py
┣ tests/
┃ ┣ base_test.py
┃ ┣ conftest.py
┃ ┣ test_channel_result_page.py
┃ ┣ test_home_page.py
┃ ┣ test_result_page.py
┃ ┣ test_search_page.py
┃ ┗ test_stream_page.py
┣ get_latest_driver.py
┣ readme.md
┣ main.py
┣ requirements.txt
┣ run.py
┗ streamer_screenshot.png
```
 
## Test run .gif


<img src="/gif/test_run.gif" width="350" height="350"/>





