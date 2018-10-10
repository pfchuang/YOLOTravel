from item.models import Itinerary
from item.models import Travel_Date

class Deposit(object):

    def __init__(self, tag_code, data_dic):
        self.tag = tag_code
        self.data_dic = data_dic
        self.count = 0

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
            'J': 'Pacific',
            'K': 'Oceania',
            'L': 'Europe',
            'M': 'MiddleAsia',
            'P': 'SouthEastAsia'  # Philippines
        }

        while self.data_dic['title']:
            self.count += 1
            item = Itinerary.objects.get_or_create(title=self.data_dic['title'].pop(),
                                            price=self.data_dic['price'].pop(),
                                            region=region[self.tag],
                                            agency='Cola',
                                            detail=self.data_dic['detail'].pop())
            travel_date = Travel_Date.objects.get_or_create(departure_date=self.data_dic['departure_date'].pop(),
                                      price=self.data_dic['date_price'].pop(),
                                      status=self.data_dic['status'].pop(),
                                      link=self.data_dic['link'].pop(),
                                      itinerary=item[0])
            print('Crawling and deposit {} data from {}'.format(self.count, self.tag))
