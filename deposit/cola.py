from item.models import Itinerary

class Deposit(object):

    def __init__(self, tag_code, items, price, year, month, day, departure_date, status, link):
        self.tag = tag_code
        self.items = items
        self.price = price
        self.year = year
        self.month = month
        self.day = day
        self.departureDate = departure_date
        self.status = status
        self.link = link

    def run(self):
        region = {
            'A': 'NorthEastAsia',  # Japan
            'B': 'NorthEastAsia',  # Korea
            'C': 'SouthEastAsia',  # Thailand
            'D': 'SouthEastAsia',  # Singapore
            'E': 'SouthEastAsia',  # Indonesia
            'F': 'SouthEastAsia',
            'G': 'China',
            'H': 'China',
            'I': 'America',
            'J': 'SouthEastAsia',
            'K': 'Oceania',
            'L': 'Europe',
            'M': 'MiddleAsia',
            'P': 'SouthEastAsia'  # Philippines
        }

        item = Itinerary.objects.get_or_create(title=self.items,
                                               year=self.year,
                                               month=self.month,
                                               day=self.day,
                                               departure_date=self.departureDate,
                                               price=self.price,
                                               region=region[self.tag],
                                               status=self.status,
                                               link=self.link,
                                               agency="Cola")