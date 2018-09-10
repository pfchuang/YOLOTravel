import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pprint import pprint
import time
import datetime
from deposit.gabriel import Deposit
from crawler.setting import Setting

class Gabriel(object):
    def __init__(self, tag_code):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        self.code = tag_code
        self.url = "http://www.gabriel.com.tw/Search?sdate=" + str(now) + "&edate=2018-12-31&country=" + tag_code
        self.data_dic = {'title':[], 'price':[], 'year':[], 'month':[], 'day':[], 'departure_date':[], 'link':[], 'status':[], 'detailed':[]}

    def content(self):
        setting = Setting()
        browser = setting.settingDriver()
        browser.get(self.url)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        for i in range(2,len(soup.select("ul[class='cue-list']"))+2):
            tmp_title = soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(2) > a")[0].text
            self.data_dic['title'].append(tmp_title)
            tmp_date = soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(1) > p")[0].text.replace('\r', '').replace('\n', '').strip()[:10]
            convertDate = datetime.date(int(tmp_date.split('/')[0]),int(tmp_date.split('/')[1]),int(tmp_date.split('/')[2]))
            self.data_dic['departure_date'].append(convertDate)
            self.data_dic['year'].append(tmp_date.split('/')[0])
            self.data_dic['month'].append(tmp_date.split('/')[1])
            self.data_dic['day'].append(tmp_date.split('/')[2])
            tmp_link = ("http://www.gabriel.com.tw" + soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(2) > a")[0]['href'])
            self.data_dic['link'].append(tmp_link)
            tmp_status = soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(5)")[0].text.split('：')[1].strip()
            self.data_dic['status'].append(tmp_status)
            tmp_price = (soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(3)")[0].text.split('：')[1])
            self.data_dic['price'].append(tmp_price)
            detailed = (browser.find_elements_by_xpath("(//div[@class='note'])"))
            day_count = 0
            dd = {}
            for item in detailed[:-1]:
                day_count += 1
                dd[('DAY ' + str(day_count))] = item.text
            self.data_dic['detailed'].append(dd)
            browser.back()
        browser.close()

    def crawl(self):
        setting = Setting()
        browser = setting.settingDriver()
        # browser = webdriver.PhantomJS()
        browser.get(self.url)
        try:
            browser.find_element_by_xpath("//a[contains(text(),'»»')]").click()
            soup = BeautifulSoup(browser.page_source, 'lxml')
            pageNum = int(soup.selecpage_sourcet("[class='pagination']")[0].find_all('a')[-1].text)
            browser.find_element_by_xpath("//a[contains(text(),'««')]").click()
            time.sleep(2)
        except IndexError:
            soup = BeautifulSoup(browser.page_source, 'lxml')
            pageNum = int(soup.select("[class='pagination']")[0].find_all('a')[-2].text)
        except:
            soup = BeautifulSoup(browser.page_source, 'lxml')
            pageNum = int(soup.select("[class='pagination']")[0].find_all('a')[0].text)
            # print(pageNum)

        soup = BeautifulSoup(browser.page_source, 'lxml')
        if pageNum > 1:
            for num in range(pageNum-1):
                self.content()
                browser.find_element_by_xpath("//a[@rel='next']").click()
                self.content()
        elif pageNum == 1:
            self.content()
        gabriel = Deposit(self.code, self.data_dic)
        gabriel.run()
