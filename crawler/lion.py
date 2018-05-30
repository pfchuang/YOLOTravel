import requests
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from item.deposit import lionDeposit

class Lion(object):
    def __init__(self, tag_code):
        self.url = 'https://travel.liontravel.com/search?Country=TW&WebCode=B2C&TravelType=1&Page=1&PageSize=1000&DepartureID=&GoDateStart=2018-05-26&GoDateEnd=2018-12-31&IsEnsureGroup=false&ArriveID=' + tag_code
        self.code = tag_code
        self.count = 0

    def crawl(self):
        res = requests.get(self.url)
        html = BeautifulSoup(res.text, 'lxml')

        items = []
        price = []
        month = []
        day = []
        status=[]
        link = []
        for item in (html.select("[class='rli_tlin m-b-sm']")):
            tmp_date = []
            tmp_title = item.select("[class='TourName']")[0].contents
            tmp_price = item.select("div[class='price']")[0].span.contents[0].strip()
            date = item.select("[class='dates_info']")[0].find_all('a')

            for i in range(len(date)):
                items.append(tmp_title[0])
                price.append(tmp_price)
                month.append(date[i].get('value').split('/')[1])
                day.append(date[i].get('value').split('/')[2])
                link.append(("https://travel.liontravel.com"+date[i].get('href')))
                if(len(date[i].contents)==1):
                    status.append("no")
                else:
                    status.append(date[i].select('span')[0].text)

        while items:
            self.count += 1
            lion = lionDeposit(self.code, items.pop(), price.pop(), month.pop(), day.pop(), status.pop(), link.pop())
            lion.run()
            print('Crawling and deposit {} data from {}'.format(self.count, self.code))
