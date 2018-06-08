from crawler.lion import Lion
from crawler.phoenix import Phoenix

def crawler_job():
    region_lion = ['--1', '--2', '--3', '--4', '--5', '--6', '--7']
    while region_lion:
        tag_code = region_lion.pop()
        lion = Lion(tag_code)
        lion.crawl()

    region_phoenix = ['EU', 'OO', 'FA', 'CN', 'AM', 'SM', 'SN', 'SS']
    while region_phoenix:
        tag_name = region_phoenix.pop()
        phoenix = Phoenix(tag_name)
        phoenix.crawl()
