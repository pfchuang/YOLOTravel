from item import models

class Deposit(object):

    def __init__(self, tag_code, items, price, month, day, status, link):
        self.tag = tag_code
        self.items = items
        self.price = price
        self.month = month
        self.day = day
        self.status = status
        self.link = link

    def run(self):
        if self.tag == '--3':
            self.europe()
        elif self.tag == '--2':
            self.oceania()
        elif self.tag == '--4':
            self.africa()
        elif self.tag == '--5':
            self.china()
        elif self.tag == '--1':
            self.america()
        elif self.tag == '--6':
            self.northeast_asia()
        elif self.tag == '--7':
            self.southeast_asia()

    def northeast_asia(self):
        item = models.NorthEastAsia(title=self.items,
                                    price=self.price,
                                    month=self.month,
                                    day=self.day,
                                    status=self.status,
                                    link=self.link,
                                    agency='Lion')
        item.save()

    def europe(self):
        item = models.Europe(title=self.items,
                             price=self.price,
                             month=self.month,
                             day=self.day,
                             status=self.status,
                             link=self.link,
                             agency='Lion')
        item.save()

    def oceania(self):
        item = models.Oceania(title=self.items,
                              price=self.price,
                              month=self.month,
                              day=self.day,
                              status=self.status,
                              link=self.link,
                              agency='Lion')
        item.save()

    def africa(self):
        item = models.Africa(title=self.items,
                             price=self.price,
                             month=self.month,
                             day=self.day,
                             status=self.status,
                             link=self.link,
                             agency='Lion')
        item.save()

    def china(self):
        item = models.China(title=self.items,
                            price=self.price,
                            month=self.month,
                            day=self.day,
                            status=self.status,
                            link=self.link,
                            agency='Lion')
        item.save()

    def america(self):
        item = models.America(title=self.items,
                             price=self.price,
                             month=self.month,
                             day=self.day,
                             status=self.status,
                             link=self.link,
                             agency='Lion')
        item.save()


    def southeast_asia(self):
        item = models.SouthEastAsia(title=self.items,
                                    price=self.price,
                                    month=self.month,
                                    day=self.day,
                                    status=self.status,
                                    link=self.link,
                                    agency='Lion')
        item.save()
