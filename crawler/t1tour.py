import requests
from bs4 import BeautifulSoup
from deposit.t1tour import Deposit
import datetime
from selenium import webdriver
from crawler.setting import Setting

class T1tour(object):
    def __init__(self, tag_code):
        now = datetime.datetime.now().strftime("%m-%d-%Y").replace('-','%2F')
        self.url = 'http://www.t1tour.com.tw/tour?country=' + tag_code + '&sdate='+str(now)+'&edate=12%2F31%2F2018'
        self.code = tag_code
        # self.count = 0
        self.data_dic = {'title':[], 'price':[], 'year':[], 'month':[], 'day':[], 'departure_date':[], 'link':[], 'status':[]}

    def getPage(self):
        res = requests.get(self.url)
        soup = BeautifulSoup(res.text, 'lxml')
        for num in soup.select("[class='dib']"):
            total_page = len(num.find_all('a'))
        return total_page-2

    def crawl(self, page):
        res = requests.get(self.url + '&cursor=' + str(page))
        html = BeautifulSoup(res.text, 'lxml')

        for item in html.find_all('tr'):
            for data in item.find_all(has_title):
                tmp_title = data.contents[0]
                tmp_link = "http://www.t1tour.com.tw" + data['href']
                self.data_dic['title'].append(tmp_title)
                self.data_dic['link'].append(tmp_link)
            for data in item.select("[class='t-price']"):
                tmp_price = data.contents[0]
                self.data_dic['price'].append(tmp_price)
            for data in item.select("[class='t-date-txt']"):
                convertDate = ''
                tmp_date = data.contents[0]
                tmp_year = data.text.split('-')[0]
                tmp_month = data.text.split('-')[1]
                tmp_day = data.text.split('-')[2]
                convertDate = datetime.date(int(tmp_year),int(tmp_month),int(tmp_day))
                self.data_dic['departure_date'].append(convertDate)
                self.data_dic['year'].append(tmp_year.strip())
                self.data_dic['month'].append(tmp_month)
                self.data_dic['day'].append(tmp_day)
            for data in item.select("[class='t-status']"):
                tmp_status = data.contents[0].text
                self.data_dic['status'].append(tmp_status)
        setting = Setting()
        browser = setting.settingDriver()
        browser.get(self.url)
        

        t1tour = Deposit(self.code, self.data_dic)
        t1tour.run()

def has_title(tag):
    return tag.has_attr('title')
