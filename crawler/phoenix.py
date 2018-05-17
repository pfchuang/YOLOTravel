#crawler test for Phoenix - Japan & Korea
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from item.models import NorthEastAsia

class Phoenix(object):

    def main(self):
        url = 'https://www.travel.com.tw/HALL/Index/SN'

        fu = UserAgent()
        headers = {'UserAgent': fu.random}
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, 'lxml')

        wait_list = []
        view_list = []
        links = soup.find('div', class_='trip').find_all('a')
        links = [link['href'] for link in links]
        links = [urljoin(resp.url, link) for link in links]
        links = list(set(links))
        wait_list += links

        while wait_list:

            link = wait_list.pop()
            if link in view_list:
                continue

            #print(link)
            view_list.append(link)

            try:
                driver = webdriver.PhantomJS()
                driver.get(link)
                driver.maximize_window()
                #driver.implicitly_wait(10)

                items = driver.find_elements(By.XPATH, '//td')
                items = [item.text for item in items]
                #print(items)

                flag = True
                while flag:
                    trip = NorthEastAsia(title=items[1], month=items[3].split('.')[0],
                         day=items[3].split('.')[1], price=items[6],
                         status=items[11], agency='Phoenix', link=link)
                    trip.save()
                    flag = False

                    if len(items) > 13:
                        items = items[13:]
                        flag = True

            except Exception as e:
                print(e)

            finally:
                driver.quit()

phoenix = Phoenix()
phoenix.main()
