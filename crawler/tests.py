from crawler.phoenix import Phoenix
from crawler.lion import Lion
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

def flush_database():
    Itinerary.objects.all().delete()
