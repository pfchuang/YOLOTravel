from selenium import webdriver

class Setting:
    def getChromeOptions(self):
        chrome_options_headless = webdriver.ChromeOptions()
        chrome_options_headless.add_argument('--headless')
        return chrome_options_headless

    def settingDriver(self):
        self.chrome_option = self.getChromeOptions()
        return webdriver.Chrome(executable_path = "./chromedriver", chrome_options = self.chrome_option)
