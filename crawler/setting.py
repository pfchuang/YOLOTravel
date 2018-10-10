from selenium import webdriver
from pathlib import Path
import datetime

class Setting(object):

    def settingDriver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

        return webdriver.Chrome(executable_path = str(Path.home()) + "/chromedriver", chrome_options = chrome_options)

    def getNowDate():
        now = datetime.datetime.now()
        return now

    def getHalfYearByNow():
        halfYearByNow = datetime.datetime.now() + datetime.timedelta(days=180)
        return halfYearByNow
