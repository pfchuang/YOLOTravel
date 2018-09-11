from item.models import Itinerary

class Deposit(object):

    def __init__(self, tag_code, data_dic):
        self.data_dic = data_dic
        self.tag = tag_code
        self.count = 0

    def run(self):
        region = {
            'JP':'NorthEastAsia',
            'CN':'China',
            'VN':'SouthEastAsia',
            'ID':'SouthEastAsia',
            'TH':'SouthEastAsia'
        }
        while self.data_dic['title']:
            self.count += 1
            item = Itinerary.objects.get_or_create(title=self.data_dic['title'].pop(),
                                                   year=self.data_dic['year'].pop(),
                                                   month=self.data_dic['month'].pop(),
                                                   day=self.data_dic['day'].pop(),
                                                   departure_date=self.data_dic['departure_date'].pop(),
                                                   price=self.data_dic['price'].pop(),
                                                   region=region[self.tag],
                                                   status=self.data_dic['status'].pop(),
                                                   link=self.data_dic['link'].pop(),
                                                   detailed=self.data_dic['detailed'].pop(),
                                                   agency='Gabriel')
            print('Crawling and deposit {} data from {}'.format(self.count, self.tag))
