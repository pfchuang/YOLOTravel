# -*- coding: UTF-8 -*-
import requests
import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.common.by import By
from deposit.cola import Deposit
from crawler.setting import Setting

now = Setting.getNowDate().strftime("%Y/%m/%d")
halfYearByNow = Setting.getHalfYearByNow().strftime("%Y/%m/%d")

class Cola(object):
    def __init__(self, tag_code):
        self.url = 'https://www.colatour.com.tw/C10A_TourSell/C10A02_TourQuery.aspx?DepartureCity=*&RegionCode=' + tag_code + '&TourType=Tour&StartTourDate=' + now + '&EndTourDate=' + halfYearByNow
        self.code = tag_code
        self.count = 0
        self.data_dic = {'title':[], 'price':[], 'departure_date':[], 'link':[], 'status':[], 'date_price': [], 'detail': []}

    def crawl(self):
        browser = Setting.settingDriver()
        browser.get(self.url)
        print(self.url)
        # res = requests.get(self.url)
        html = BeautifulSoup(browser.page_source, 'lxml')

        available = []
        waiting = []
        datas = []

        for i in range(len(html.select("[name='ColaPager$ddlPageNo']")[0].find_all('option'))):
            self.count+=1
            html = BeautifulSoup(browser.page_source, 'lxml')
            for data in html.select("[class='Grid']"):
                for item in data.select("[class='TourName']"):
                    # pprint(item.text)
                    self.data_dic['title'].append(item.text)
                    tmp_link = "https://www.colatour.com.tw"+str(item['href'])
                    self.data_dic['link'].append(tmp_link)
                    browser.get(tmp_link)
                    detail = browser.find_elements_by_xpath("//td[@style='background-color: #D1E6FE; color: blue']")
                    day_count = 0
                    detail_dic = {}
                    for detail_data in detail:
                        day_count += 1
                        detail_dic[("DAY " + str(day_count))] = detail_data.text
                    browser.back()
                    self.data_dic['detail'].append(detail_dic)
            for item in html.select("[class='GridItem']"):
                tmp_data = item.text.replace("\n", "").replace("\r", "").replace("  ", "")
                datas.append(tmp_data)


            browser.find_element_by_xpath("//input[@id='ColaPager_cmdNextPage']").click()
            print('Preparing {} data from {}'.format(self.count, self.code))
        browser.quit()
        # pprint(datas)
        count_seat=-1
        for i in range(len(datas)):
            if i%11==2:
                tmp_month = datas[i].split('/')[0]
                tmp_day = datas[i].split('/')[1][:2]
                tmp_date = datetime.date(2018, int(tmp_month), int(tmp_day))
                self.data_dic['departure_date'].append(tmp_date)
            elif i%11==6:
                self.data_dic['price'].append(datas[i])
                self.data_dic['date_price'].append(datas[i])
            elif i%11==8:
                available.append(datas[i])
                count_seat+=1
            elif i%11==9:
                waiting.append(datas[i])
            elif i%11==10:
                if(datas[i]!="關團"):
                    tmp_string="可售:"+available[count_seat]+" 候補:"+waiting[count_seat]
                    self.data_dic['status'].append(tmp_string)
                else:
                    self.data_dic['status'].append(datas[i])
            
        cola = Deposit(self.code, self.data_dic)
        cola.run()

