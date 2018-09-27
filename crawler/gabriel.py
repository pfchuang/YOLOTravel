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
        self.data_dic = {'title':'', 'price':'', 'departure_date':[], 'link':[], 'status':[], 'detail':{}}
        self.items = []
        self.count = 0

    def resetDataDic(self):
        self.data_dic = {'title':'', 'price':'', 'departure_date':'', 'link':'', 'status':'', 'detail':{}, 'date_price':''}

    def content(self):
        setting = Setting()
        browser = setting.settingDriver()
        browser.get(self.url)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        for i in range(2,len(soup.select("ul[class='cue-list']"))+2):
            tmp_title = soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(2) > a")[0].text
            self.data_dic['title'] = tmp_title
            tmp_date = soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(1) > p")[0].text.replace('\r', '').replace('\n', '').strip()[:10]
            convertDate = datetime.date(int(tmp_date.split('/')[0]),int(tmp_date.split('/')[1]),int(tmp_date.split('/')[2]))
            self.data_dic['departure_date'] = convertDate
            tmp_link = ("http://www.gabriel.com.tw" + soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(2) > a")[0]['href'])
            self.data_dic['link'] = tmp_link
            tmp_status = soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(5)")[0].text.split('：')[1].strip()
            self.data_dic['status'] = tmp_status
            tmp_price = (soup.select("div.out-showcue-list > ul:nth-of-type(" + str(i) + ") > li:nth-of-type(3)")[0].text.split('：')[1])
            self.data_dic['price'] = tmp_price
            self.data_dic['date_price'] = tmp_price
            browser.get(tmp_link)
            detail = (browser.find_elements_by_xpath("(//div[@class='note'])"))
            keyword = (browser.find_elements_by_tag_name('h6'))[:-1]
            key = []
            day_count = 0
            detail_dic = {}
            for item in detail[:-1]:
                day_count += 1
                detail_dic[("DAY " + str(day_count))] = item.text
            for item in keyword:
                if(item.text != ''):
                    key.append(item.text)
                    detail_dic['keywords'] = key
            self.data_dic['detail'] = detail_dic
            self.items.append(self.data_dic)
            self.resetDataDic()
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
        while self.items:
            self.count += 1
            gabriel = Deposit(self.code, self.items.pop())
            gabriel.run()
            print('Crawling and deposit {} data from {}'.format(self.count, self.code))
