import requests
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime
from deposit.lion import Deposit

class Lion(object):
    def __init__(self, tag_code):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        self.url = "https://travel.liontravel.com/search?Country=TW&WebCode=B2C&TravelType=1&Page=1&PageSize=1000&DepartureID=&GoDateStart="+ now + "&GoDateEnd=2018-12-31&IsEnsureGroup=false&ArriveID" + tag_code
        self.code = tag_code
        self.count = 0
        self.data_dic = {'title':[], 'price':[], 'year':[], 'month':[], 'day':[], 'departure_date':[], 'link':[], 'status':[], 'detailed':[]}


    def crawl(self):
        res = requests.get(self.url)
        html = BeautifulSoup(res.text, 'lxml')

        items = []
        price = []
        month = []
        day = []
        status=[]
        link = []
        year = []
        convertDate = ''
        departureDate = []
        for item in (html.select("[class='rli_tlin m-b-sm']")):
            tmp_date = []
            tmp_title = item.select("[class='TourName']")[0].contents
            tmp_price = item.select("div[class='price']")[0].span.contents[0].strip().strip('$')
            date = item.select("[class='dates_info']")[0].find_all('a')
            self.data_dic['title'].append(tmp_title[0]) 
            self.data_dic['link'].append(("https://travel.liontravel.com"+date[i].get('href')))
            if(len(date[i].contents)==1):
                self.data_dic['status'].append("no")
            else:
                self.data_dic['status'].append(date[i].select('span')[0].text)

            for i in range(len(date)):
                tmp_month = date[i].get('value').split('/')[1]
                tmp_day = date[i].get('value').split('/')[2]
                

                self.data_dic['year'].append('2018')
                self.data_dic['price'].append(tmp_price)
                self.data_dic['month'].append(tmp_month)
                self.data_dic['day'].append(tmp_day)
                convertDate = datetime.date(2018,int(tmp_month),int(tmp_day))
                self.data_dic['departure_date'].append(convertDate)
                
        lion = Deposit(self.code, self.data_dic)
        lion.run()

        
