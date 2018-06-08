from django.db import models

# Create your models here.
class Itinerary(models.Model):
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    price = models.CharField(max_length=6)
    region = models.CharField(max_length=13)
    agency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
