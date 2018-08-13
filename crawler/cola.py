import requests
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from deposit.cola import Deposit

class Cola(object):
    def __init__(self, tag_code):
        now = datetime.datetime.now().strftime("%Y-%m-%d").replace('-', '/')
        self.url = 'https://www.colatour.com.tw/C10A_TourSell/C10A02_TourQuery.aspx?DepartureCity=*&RegionCode=' + tag_code + '&TourType=Tour&StartTourDate=' + now + '&EndTourDate=2018/08/31'
        self.code = tag_code
        self.count = 0


    def crawl(self):
        browser = webdriver.PhantomJS()
        browser.get(self.url)
        # res = requests.get(self.url)
        html = BeautifulSoup(browser.page_source, 'lxml')

        tmp_data = ""
        tmp_string=""
        items=[]
        available = []
        waiting = []
        datas = []
        departureDate = []
        status = []
        price = []
        year = []
        month = []
        day = []
        link = []

        for i in range(len(html.select("[name='ColaPager$ddlPageNo']")[0].find_all('option'))):
            html = BeautifulSoup(browser.page_source, 'lxml')
            for data in html.select("[class='Grid']"):
                for item in data.select("[class='TourName']"):
                    # pprint(item.text)
                    items.append(item.text)
                    link.append("https://www.colatour.com.tw/"+str(item['href']))
                    year.append('2018')
            for item in html.select("[class='GridItem']"):
                tmp_data = item.text.replace("\n", "").replace("\r", "").replace("  ", "")
                datas.append(tmp_data)


            browser.find_element_by_xpath("//input[@id='ColaPager_cmdNextPage']").click()
        browser.quit()
        # pprint(datas)
        count_seat=-1
        for i in range(len(datas)):
            if i%11==2:
                tmp_month = datas[i].split('/')[0]
                month.append(tmp_month)
                tmp_day = datas[i].split('/')[1][:2]
                day.append(tmp_day)
                tmp_date = datetime.date(2018, int(tmp_month), int(tmp_day))
                departureDate.append(tmp_date)
            elif i%11==6:
                price.append(datas[i])
            elif i%11==8:
                available.append(datas[i])
                count_seat+=1
            elif i%11==9:
                waiting.append(datas[i])
            elif i%11==10:
                if(datas[i]!="關團"):
                    tmp_string="可售:"+available[count_seat]+" 候補:"+waiting[count_seat]
                    status.append(tmp_string)
                else:
                    status.append(datas[i])

        while items:
            self.count += 1
            cola = Deposit(self.code, items.pop(), price.pop(), year.pop(), month.pop(), day.pop(), departureDate.pop(), status.pop(), link.pop())
            cola.run()
            print('Crawling and deposit {} data from {}'.format(self.count, self.code))
