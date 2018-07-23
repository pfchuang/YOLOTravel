import requests
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime
# from deposit.lion import Deposit

class Cola(object):
    def __init__(self, tag_code):
        self.url = 'https://www.colatour.com.tw/C10A_TourSell/C10A02_TourQuery.aspx?DepartureCity=*&RegionCode=A&TourType=Tour&StartTourDate=2018/06/14&EndTourDate=2018/6/30'
        self.code = tag_code
        self.count = 0


    def crawl(self):
        res = requests.get(self.url)
        html = BeautifulSoup(res.text, 'lxml')

        title = []
        price = []
        month = []
        day = []
        status=[]
        link = []
        year = []
        aaaa = []
