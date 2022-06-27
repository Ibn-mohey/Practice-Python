import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import random
import threading as th
import re
import urllib.request
chrome_path = "chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=chrome_path)
website = 'https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&view_all_page_id=719853864726295&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=page&media_type=all'
driver.get(website)

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(2)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

pages = driver.find_elements(by=By.CSS_SELECTOR, value='div[class="_99s5"]')

links = []
names = []
count = 0
i = 0
for page in pages:
#     print(i)
    try:
        video_url = page.find_element(by=By.CSS_SELECTOR, value='video').get_attribute("src")
        links.append(video_url)
        video_name = re.findall('\/(\d+_\d+_\d+_n)' ,video_url)[0]
        video_name += '.mp4'
        names.append(video_name)
        urllib.request.urlretrieve(video_url, video_name)
    except:
        pass