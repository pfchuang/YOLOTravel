from crawler.phoenix import Phoenix

def phoenix_test():
    region = ['EU', 'OO', 'FA', 'CN', 'AM', 'SM', 'SN', 'SS']
    while region:
        tag_name = region.pop()
        phoenix = Phoenix(tag_name)
        phoenix.crawl()
