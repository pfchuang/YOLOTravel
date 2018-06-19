from crawler.lion import Lion
from crawler.phoenix import Phoenix
from crawler.t1tour import T1tour

def crawler_job():
    region_lion = ['--1', '--2', '--3', '--4', '--5', '--6', '--7']
    while region_lion:
        tag_code = region_lion.pop()
        lion = Lion(tag_code)
        lion.crawl()

    region_t1 = ['1', '2', '3', '4', '5', '6', '8', '15', '17']
    while region_t1:
        tag_code = region_t1.pop()
        t1tour = T1tour(tag_code)
        total_page = t1tour.getPage()
        for i in range(1,total_page+1):
            t1tour.crawl(i)

    region_phoenix = ['EU', 'OO', 'FA', 'CN', 'AM', 'SM', 'SN', 'SS']
    while region_phoenix:
        tag_name = region_phoenix.pop()
        phoenix = Phoenix(tag_name)
        phoenix.crawl()

    region_t1tour = ['1', '2', '3', '4', '5', '6', '8', '15', '17']
    while region_t1tour:
        tag_code = region.pop()
        t1tour = T1tour(tag_code)
        total_page = t1tour.getPage()
        for i in range(1,total_page+1):
            t1tour.crawl(i)
