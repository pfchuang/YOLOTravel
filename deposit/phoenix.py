from item.models import Itinerary
from item.models import Travel_Date
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

        item = Itinerary.objects.create(title=self.items[1],
                                        price=self.items[6],
                                        region=region[self.tag],
                                        detail='',
                                        agency='Phoenix')
        travel_date = Travel_Date.objects.create(departure_date=self.convertDate,
                                    price=self.items[6],
                                    status=self.items[11],
                                    link=self.link,
                                    itinerary=item)
