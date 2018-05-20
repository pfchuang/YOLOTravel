from item import models

class phoenixDeposit(object):

    def __init__(self, tag_name, items, link):
        self.tag = tag_name
        self.items = items
        self.link = link

    def run(self):
        if self.tag == 'EU':
            self.europe()
        elif self.tag == 'OO':
            self.oceania()
        elif self.tag == 'FA':
            self.africa()
        elif self.tag == 'CN':
            self.china()
        elif self.tag == 'AM':
            self.america()
        elif self.tag == 'SM':
            self.middle_asia()
        elif self.tag == 'SN':
            self.northeast_asia()
        elif self.tag == 'SS':
            self.southeast_asia()

    def northeast_asia(self):
        items = self.items
        item = models.NorthEastAsia(title=items[1], month=items[3].split('.')[0],
                                    day=items[3].split('.')[1], price=items[6],
                                    status=items[11], agency='Phoenix', link=self.link)
        item.save()

    def europe(self):
        items = self.items
        item = models.Europe(title=items[1], month=items[3].split('.')[0],
                             day=items[3].split('.')[1], price=items[6],
                             status=items[11], agency='Phoenix', link=self.link)
        item.save()

    def oceania(self):
        items = self.items
        item = models.Oceania(title=items[1], month=items[3].split('.')[0],
                              day=items[3].split('.')[1], price=items[6],
                              status=items[11], agency='Phoenix', link=self.link)
        item.save()

    def africa(self):
        items = self.items
        item = models.Africa(title=items[1], month=items[3].split('.')[0],
                             day=items[3].split('.')[1], price=items[6],
                             status=items[11], agency='Phoenix', link=self.link)
        item.save()

    def china(self):
        items = self.items
        item = models.China(title=items[1], month=items[3].split('.')[0],
                            day=items[3].split('.')[1], price=items[6],
                            status=items[11], agency='Phoenix', link=self.link)
        item.save()

    def america(self):
        items = self.items
        item = models.America(title=items[1], month=items[3].split('.')[0],
                              day=items[3].split('.')[1], price=items[6],
                              status=items[11], agency='Phoenix', link=self.link)
        item.save()

    def middle_asia(self):
        items = self.items
        item = models.MiddleAsia(title=items[1], month=items[3].split('.')[0],
                                 day=items[3].split('.')[1], price=items[6],
                                 status=items[11], agency='Phoenix', link=self.link)
        item.save()

    def southeast_asia(self):
        items = self.items
        item = models.SouthEastAsia(title=items[1], month=items[3].split('.')[0],
                                    day=items[3].split('.')[1], price=items[6],
                                    status=items[11], agency='Phoenix', link=self.link)
        item.save()
