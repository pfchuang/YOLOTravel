from item.models import Itinerary
from item.models import Travel_Date

class Deposit(object):

    def __init__(self, tag_code, data_dic):
        self.data_dic = data_dic
        self.tag = tag_code

    def run(self):
        region = {
            'JP':'NorthEastAsia',
            'CN':'China',
            'VN':'SouthEastAsia',
            'ID':'SouthEastAsia',
            'TH':'SouthEastAsia'
        }

        item = Itinerary.objects.create(title=self.data_dic['title'],
                                        price=self.data_dic['price'],
                                        region=region[self.tag],
                                        detail=self.data_dic['detail'],
                                        agency='Gabriel')
        travel_date = Travel_Date.objects.create(departure_date=self.data_dic['departure_date'],
                                    price=self.data_dic['date_price'],
                                    status=self.data_dic['status'],
                                    link=self.data_dic['link'],
                                    itinerary=item)  
        
