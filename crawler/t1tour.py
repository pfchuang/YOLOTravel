import requests
from bs4 import BeautifulSoup
from deposit.t1tour import Deposit
import datetime
from selenium import webdriver
from crawler.setting import Setting

now = Setting.getNowDate().strftime("%m-%d-%Y").replace('-','%2F')
halfYearByNow = Setting.getHalfYearByNow().strftime("%m-%d-%Y").replace('-','%2F')

class T1tour(object):
    def __init__(self, tag_code):
        self.url = 'http://www.t1tour.com.tw/tour?country=' + tag_code + '&sdate=' + now + '&edate=' + halfYearByNow
        self.code = tag_code
        # self.count = 0
        self.data_dic = {'title':[], 'price':[], 'departure_date':[], 'link':[], 'status':[], 'date_price': [], 'detail': []}

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
                detail_res = requests.get(tmp_link)
                soup = BeautifulSoup(detail_res.text, 'lxml')
                detail = soup.select("div[class='dailyTitle']")
                keyword = soup.select("div[class='editorTxt col-sm-12']")
                key = []
                day_count = 0
                detail_dic = {}

                for schedule in detail:
                    day_count += 1
                    detail_dic[("DAY " + str(day_count))] = schedule.text.replace('\n', '')
                for word in keyword:
                    if(word.find('h4')!=None):
                        key.append(word.find('h4').text.replace('\xa0',' '))
                        detail_dic['Keywords'] = key
                self.data_dic['detail'].append(detail_dic)
            for data in item.select("[class='t-price']"):
                tmp_price = data.contents[0]
                self.data_dic['price'].append(tmp_price)
                self.data_dic['date_price'].append(tmp_price)
            for data in item.select("[class='t-date-txt']"):
                convertDate = ''
                tmp_date = data.contents[0]
                tmp_year = data.text.split('-')[0]
                tmp_month = data.text.split('-')[1]
                tmp_day = data.text.split('-')[2]
                convertDate = datetime.date(int(tmp_year),int(tmp_month),int(tmp_day))
                self.data_dic['departure_date'].append(convertDate)
            for data in item.select("[class='t-status']"):
                tmp_status = data.contents[0].text
                self.data_dic['status'].append(tmp_status)

        t1tour = Deposit(self.code, self.data_dic)
        t1tour.run()

def has_title(tag):
    return tag.has_attr('title')
