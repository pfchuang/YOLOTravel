from item.models import Itinerary

class Deposit(object):

    def __init__(self, tag_code, items, price, month, day, status, link):
        self.tag = tag_code
        self.items = items
        self.price = price
        self.month = month
        self.day = day
        self.status = status
        self.link = link

    def run(self):
        region = {
            '--3': 'Europe',
            '--2': 'Oceania',
            '--4': 'Africa',
            '--5': 'China',
            '--1': 'America',
            '--6': 'NorthEastAsia',
            '--7': 'SouthEastAsia'
        }

        item = Itinerary.objects.get_or_create(title=self.items,
                                               month=self.month,
                                               day=self.day,
                                               price=self.price,
                                               region=region[self.tag],
                                               status=self.status,
                                               link=self.link,
                                               agency='Lion')
