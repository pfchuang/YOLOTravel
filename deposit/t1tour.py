from item.models import Itinerary
from item.models import Travel_Date

class Deposit(object):

    def __init__(self, tag_code, data_dic):
        self.data_dic = data_dic
        self.tag = tag_code
        self.count = 0

    def run(self):
        region = {
            '1':'Europe',
            '2':'Europe',
            '3':'Europe',
            '4':'Europe',
            '5':'Europe',
            '6':'Europe',
            '8':'Europe',
            '15':'Europe',
            '17':'Europe'
        }
        while self.data_dic['title']:
            self.count += 1
            item = Itinerary.objects.create(title=self.data_dic['title'].pop(),
                                            price=self.data_dic['price'].pop(),
                                            region=region[self.tag],
                                            agency='TOneTour',
                                            detail=self.data_dic['detail'].pop())
            travel_date = Travel_Date.objects.create(departure_date=self.data_dic['departure_date'].pop(),
                                      price=self.data_dic['date_price'].pop(),
                                      status=self.data_dic['status'].pop(),
                                      link=self.data_dic['link'].pop(),
                                      itinerary=item)
            print('Crawling and deposit {} data from {}'.format(self.count, self.tag))
