import requests
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime
from deposit.lion import Deposit
from selenium import webdriver
from crawler.setting import Setting
class Lion(object):
    def __init__(self, tag_code):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        self.url = "https://travel.liontravel.com/search?Country=TW&WebCode=B2C&TravelType=1&Page=1&PageSize=1000&DepartureID=&GoDateStart="+ now + "&GoDateEnd=2018-10-05&IsEnsureGroup=false&ArriveID=" + tag_code
        print(self.url)
        self.code = tag_code
        self.count = 0
        self.itinerary = {'title':'', 'price':'', 'detail':{}, 'departure_date':[],'link':[], 'status':[], 'date_price':[]}
    
    def resetItinerary(self):
        self.itinerary = {'title':'', 'price':'', 'detail':{},'departure_date':[],'link':[], 'status':[], 'date_price':[]}
    
    def crawl(self):
        res = requests.get(self.url)
        html = BeautifulSoup(res.text, 'lxml')
        items = []
        convertDate = ''
        for item in (html.select("[class='rli_tlin m-b-sm']")):
            self.count += 1
            tmp_title = item.select("[class='TourName']")[0].contents
            tmp_price = item.select("div[class='price']")[0].span.contents[0].strip().strip('$')
            date = item.select("[class='dates_info']")[0].find_all('a')
            for i in range(len(date)):
                tmp_date = date[i].text[:5].split('/') #ex:12/21
                convertDate = datetime.date(2018,int(tmp_date[0]),int(tmp_date[1]))
                self.itinerary['departure_date'].append(convertDate)
                tmp_link = ("https://travel.liontravel.com"+date[i].get('href'))
                self.itinerary['link'].append(tmp_link)
                self.itinerary['date_price'].append(tmp_price) #不同日期需要不同價格（須修改）
                if(len(date[i].contents)==1):
                    self.itinerary['status'].append("no")
                else:
                    self.itinerary['status'].append(date[i].select('span')[0].text)
            self.itinerary['price'] = tmp_price
            self.itinerary['title'] = tmp_title[0]
            self.getDetail(tmp_link)

            items.append(self.itinerary)
            self.resetItinerary() #reset itinerary to empty
            print('Crawling and deposit {} data from {}'.format(self.count, self.code))
        while items:
            tmp_itin = items.pop()
            lion = Deposit(self.code, items.pop())
            lion.run()
            

    def getDetail(self, link):
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'lxml')
        try:
            detail = soup.select("[class='clp-subtitle font-16']")
            day_count = 0
            detail_dic = {}
            for item in detail:
                day_count += 1
                detail_dic[("DAY " + str(day_count))] = item.text
            self.itinerary['detail'] = detail_dic
        except:
            no_detail = {"notice":"此項目無行程內容"}
            self.itinerary['detail'] = no_detail

        # setting = Setting()
        # browser = setting.settingDriver()
        # browser.get(self.url)
        # try:
        #     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
        #     browser.find_element_by_xpath("//a[contains(text(),'行程内容')]").click()
        #     detail = (browser.find_elements_by_xpath("//div[@class='clp-header md-top-n']/p[2]"))
        #     day_count = 0
        #     detail_dic = {}
        #     for item in detail:
        #         day_count += 1
        #         detail_dic[("DAY " + str(day_count))] = item.text
        #     self.itinerary['detail'] = detail_dic
        # except:
        #     no_detail = {"notice":"此項目無行程內容"}
        #     self.itinerary['detail'] = no_detail
        # browser.close()




