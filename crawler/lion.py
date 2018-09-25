import requests
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime
from deposit.lion import Deposit

class Lion(object):
<<<<<<< HEAD
   def __init__(self, tag_code):
       now = datetime.datetime.now().strftime("%Y-%m-%d")
       self.url = "https://travel.liontravel.com/search?Country=TW&WebCode=B2C&TravelType=1&Page=1&PageSize=1000&DepartureID=&GoDateStart="+ now + "&GoDateEnd=2018-12-31&IsEnsureGroup=false&ArriveID" + tag_code
       self.code = tag_code
       self.count = 0
       self.data_dic = {'title':[], 'price':[], 'year':[], 'month':[], 'day':[], 'departure_date':[], 'link':[], 'status':[], 'detailed':[]}


   def crawl(self):
       res = requests.get(self.url)
       html = BeautifulSoup(res.text, 'lxml')
       
       convertDate = ''
       for item in (html.select("[class='rli_tlin m-b-sm']")):
           tmp_date = []
           tmp_title = item.select("[class='TourName']")[0].contents
           tmp_price = item.select("div[class='price']")[0].span.contents[0].strip().strip('$')
           date = item.select("[class='dates_info']")[0].find_all('a')

           for i in range(len(date)):
               tmp_month = date[i].get('value').split('/')[1]
               tmp_day = date[i].get('value').split('/')[2]
               self.data_dic['title'].append(tmp_title[0])
               self.data_dic['year'].append('2018')
               self.data_dic['price'].append(tmp_price)
               self.data_dic['month'].append(tmp_month)
               self.data_dic['day'].append(tmp_day)
               convertDate = datetime.date(2018,int(tmp_month),int(tmp_day))
               self.data_dic['departure_date'].append(convertDate)
               self.data_dic['link'].append(("https://travel.liontravel.com"+date[i].get('href')))
               if(len(date[i].contents)==1):
                   self.data_dic['status'].append("no")
               else:
                   self.data_dic['status'].append(date[i].select('span')[0].text)

       lion = Deposit(self.code, self.data_dic)
       lion.run()
=======
    def __init__(self, tag_code):
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        self.url = "https://travel.liontravel.com/search?Country=TW&WebCode=B2C&TravelType=1&Page=1&PageSize=1000&DepartureID=&GoDateStart="+ now + "&GoDateEnd=2018-12-31&IsEnsureGroup=false&ArriveID=" + tag_code
        print(self.url)
        self.code = tag_code
        self.count = 0
        self.itinerary = {'title':'', 'price':'', 'detailed':'','departure_date':[],'link':[], 'status':[], 'date_price':[]}
    
    def resetItinerary(self):
        self.itinerary = {'title':'', 'price':'', 'detailed':'','departure_date':[],'link':[], 'status':[], 'date_price':[]}
    
    def crawl(self):
        res = requests.get(self.url)
        html = BeautifulSoup(res.text, 'lxml')
        items = []
        convertDate = ''
        for item in (html.select("[class='rli_tlin m-b-sm']")):
            tmp_title = item.select("[class='TourName']")[0].contents
            tmp_price = item.select("div[class='price']")[0].span.contents[0].strip().strip('$')
            date = item.select("[class='dates_info']")[0].find_all('a')
            for i in range(len(date)):
                tmp_date = date[i].text[:5].split('/') #ex:12/21
                convertDate = datetime.date(2018,int(tmp_date[0]),int(tmp_date[1]))
                self.itinerary['departure_date'].append(convertDate)
                self.itinerary['link'].append(("https://travel.liontravel.com"+date[i].get('href')))
                self.itinerary['date_price'].append(tmp_price) #不同日期需要不同價格（須修改）
                if(len(date[i].contents)==1):
                    self.itinerary['status'].append("no")
                else:
                    self.itinerary['status'].append(date[i].select('span')[0].text)
            self.itinerary['price'] = tmp_price
            self.itinerary['title'] = tmp_title[0]
            items.append(self.itinerary)
            self.resetItinerary() #reset itinerary to empty
        while items:
            self.count += 1
            tmp_itin = items.pop()
            lion = Deposit(self.code, tmp_itin['title'], tmp_itin['price'], 
                            tmp_itin['departure_date'], tmp_itin['status'], tmp_itin['link'], tmp_itin['date_price'])
            lion.run()
            print('Crawling and deposit {} data from {}'.format(self.count, self.code))
>>>>>>> 4c842ad27bbac2e170d053cbfdc26ec43b4572d6
