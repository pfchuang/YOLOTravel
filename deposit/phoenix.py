from item.models import Itinerary
import datetime

class Deposit(object):

    def __init__(self, tag_name, items, link):
        self.tag = tag_name
        self.items = items
        self.link = link

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
        convertDate = ""
        convertDate = datetime.date(2018,int(items[3].split('.')[0]),int(items[3].split('.')[1]))
        item = Itinerary.objects.get_or_create(title=items[1],year="2018", month=items[3].split('.')[0],
                                               day=items[3].split('.')[1],departure_date=convertDate,
                                               price=items[6], region=region[self.tag],
                                               status=items[11], agency='Phoenix', link=self.link)
