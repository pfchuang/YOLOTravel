from django.db import models
from django.urls import reverse

# Create your models here.
class Itinerary(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.CharField(max_length=6)
    region = models.CharField(max_length=13)
    agency = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    detail = models.TextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_travel_detail(self):
        return reverse('Item:travel_data_detail', args = [self.id])

class Travel_Date(models.Model):
    departure_date = models.DateField()
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    price = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
