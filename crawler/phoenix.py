# -*- coding: utf-8 -*-
import requests
import datetime

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from deposit.phoenix import Deposit

class Phoenix(object):

    def __init__(self, tag_name):
        self.url = 'https://www.travel.com.tw/HALL/Index/' + tag_name
        self.tag = tag_name
        self.count = 0

    def crawl(self):
        fu = UserAgent()
        headers = {'UserAgent': fu.random}
        resp = requests.get(self.url, headers=headers)
        html = BeautifulSoup(resp.text, 'lxml')

        links = html.find('div', class_='trip').find_all('a')
        links = [link['href'] for link in links]
        links = [urljoin(resp.url, link) for link in links]
        links = list(set(links))

        wait_list = []
        wait_list += links
        while wait_list:
            link = wait_list.pop()
            driver = webdriver.PhantomJS()
            driver.get(link)
            items = driver.find_elements(By.XPATH, '//td')
            items = [item.text for item in items]

            flag = True
            while flag:
                if items == None or len(items) < 13:
                    break
                if items[11] == u'結團':
                    if len(items) == 13:
                        break
                    items = items[13:]
                    flag = True
                    continue
                self.count += 1
                convertDate = datetime.date(2018, int(items[3].split('.')[0]), int(items[3].split('.')[1]))
                phoenix = Deposit(self.tag, items, link, convertDate)
                phoenix.run()
                print('Crawling and deposit {} data from {}'.format(self.count, self.tag))
                flag = False

            driver.quit()

        # try:
        #     driver = webdriver.PhantomJS()
        #     driver.get(link)
        #     items = driver.find_elements(By.XPATH, '//td')
        #     items = [item.text for item in items]
        #
        #     flag = True
        #     while flag:
        #         self.count += 1
        #         phoenix = phoenixDeposit(self.tag, items, link)
        #         phoenix.run()
        #         print('Crawling and deposit {} data from {}'.format(self.count, self.tag))
        #         flag = False
        #         # if len(items) > 13:
        #         #     items = items[13:]
        #         #     flag = True
        #
        # except Exception as e:
        #     print(e)
        #
        # finally:
        #     driver.quit()
