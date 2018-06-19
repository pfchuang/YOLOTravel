from item.models import Itinerary
import datetime

class Deposit(object):

    def __init__(self, tag_name, items, link, convertDate):
        self.tag = tag_name
        self.items = items
        self.link = link
        self.convertDate = convertDate

    def run(self):
        region = {
            'EU': 'Europe',
            'OO': 'Oceania',
            'FA': 'Africa',
            'CN': 'China',
            'AM': 'America',
            'SM': 'MiddleAsia',
            'SN': 'NorthEastAsia',
            'SS': 'SouthEastAsia'
        }

        items = self.items
        item = Itinerary.objects.get_or_create(title=items[1], year='2018', month=items[3].split('.')[0],
                                               day=items[3].split('.')[1], price=items[6], region=region[self.tag],
                                               status=items[11], agency='Phoenix', link=self.link, departure_date=self.convertDate)
