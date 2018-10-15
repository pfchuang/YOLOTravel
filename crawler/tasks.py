from crawler.lion import Lion
from crawler.phoenix import Phoenix
from crawler.t1tour import T1tour
from crawler.cola import Cola
from crawler.gabriel import Gabriel

def crawler_job():

    region_t1tour = ['1', '2', '3', '4', '5', '6', '8', '15', '17']
    while region_t1tour:
        tag_t1tour = region_t1tour.pop()
        t1tour = T1tour(tag_t1tour)
        total_page = t1tour.getPage()
        for i in range(1,total_page+1):
            t1tour.crawl(i)

    region_cola = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'P']
    while region_cola:
        tag_cola = region_cola.pop()
        cola = Cola(tag_cola)
        cola.crawl()

    region_gabriel = ['JP', 'CN', 'VN', 'ID', 'TH']
    while region_gabriel:
        tag_gabriel = region_gabriel.pop()
        gabriel = Gabriel(tag_gabriel)
        gabriel.crawl()

    region_lion = ['--1', '--2', '--3', '--4', '--5', '--6', '--7']
    while region_lion:
        tag_lion = region_lion.pop()
        lion = Lion(tag_lion)
        lion.crawl()

    region_phoenix = ['EU', 'OO', 'FA', 'CN', 'AM', 'SM', 'SN', 'SS']
    while region_phoenix:
        tag_phoenix = region_phoenix.pop()
        phoenix = Phoenix(tag_phoenix)
        phoenix.crawl()
