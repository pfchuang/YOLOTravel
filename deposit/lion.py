from item.models import Itinerary
from item.models import Travel_Date

class Deposit(object):

    def __init__(self, tag_code, title, price, departure_date, status, link, date_price):
        self.tag = tag_code
        self.title = title
        self.price = price
        self.departureDate = departure_date
        self.status = status
        self.link = link
        self.date_price = date_price

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

        item = Itinerary.objects.create(title=self.title,
                         price=self.price,
                         region=region[self.tag],
                         agency='Lion',
                         detailed='')
        for i in range(len(self.departureDate)):
            travel_date = Travel_Date.objects.create(departure_date=self.departureDate[i],
                                      price=self.date_price[i],
                                      status=self.status[i],
                                      link=self.link[i],
                                      itinerary=item)                                 
                                               
