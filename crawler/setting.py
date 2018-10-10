from selenium import webdriver
from pathlib import Path

class Setting:
    def getChromeOptions(self):
        chrome_options_headless = webdriver.ChromeOptions()
        chrome_options_headless.add_argument('--headless')
        chrome_options_headless.add_argument('--disable-gpu')
        return chrome_options_headless

    def settingDriver(self):
        self.chrome_option = self.getChromeOptions()
        return webdriver.Chrome(executable_path = str(Path.home()) + "/chromedriver", chrome_options = self.chrome_option)
