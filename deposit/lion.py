from item.models import Itinerary
from item.models import Travel_Date

class Deposit(object):

    def __init__(self, tag_code, itinerary):
        self.tag = tag_code
        self.itinerary = itinerary
        # self.title = title
        # self.price = price
        # self.departureDate = departure_date
        # self.status = status
        # self.link = link
        # self.date_price = date_price

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

        item = Itinerary.objects.create(title=self.itinerary['title'],
                         price=self.itinerary['price'],
                         region=region[self.tag],
                         agency='Lion',
                         detail=self.itinerary['detail'])
        for i in range(len(self.itinerary['departure_date'])):
            travel_date = Travel_Date.objects.create(departure_date=self.itinerary['departure_date'],
                                      price=self.itinerary['date_price'],
                                      status=self.itinerary['status'],
                                      link=self.itinerary['link'],
                                      itinerary=item)                                 
                                               
