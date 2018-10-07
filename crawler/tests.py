from crawler.phoenix import Phoenix
from crawler.lion import Lion
from crawler.cola import Cola
from crawler.t1tour import T1tour
from crawler.gabriel import Gabriel
from item.models import Itinerary

def phoenix_test():
    region = ['EU', 'OO', 'FA', 'CN', 'AM', 'SM', 'SN', 'SS']
    while region:
        tag_name = region.pop()
        phoenix = Phoenix(tag_name)
        phoenix.crawl()

def lion_test():
    region = ['--1', '--2', '--3', '--4', '--5', '--6', '--7']
    while region:
        tag_code = region.pop()
        lion = Lion(tag_code)
        lion.crawl()

def cola_test():
    region = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'P']
    while region:
        tag_code = region.pop()
        cola = Cola(tag_code)
        cola.crawl()

def t1tour_test():
    region = ['1', '2', '3', '4', '5', '6', '8', '15', '17']
    while region:
        tag_code = region.pop()
        t1tour = T1tour(tag_code)
        total_page = t1tour.getPage()
        for i in range(1,total_page+1):
            t1tour.crawl(i)

def gabriel_test():
    region = ['JP', 'CN', 'VN', 'ID', 'TH']
    while region:
        tag_code = region.pop()
        gabriel = Gabriel(tag_code)
        gabriel.crawl()

def flush_database():
    Itinerary.objects.all().delete()
