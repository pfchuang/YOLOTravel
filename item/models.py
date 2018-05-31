from django.db import models

# Create your models here.
class NorthEastAsia(models.Model):
    region = "North East Asia"
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    price = models.CharField(max_length=6)
    agency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Europe(models.Model):
    region = "Europe"
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    price = models.CharField(max_length=6)
    agency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Oceania(models.Model):
    region = "Oceania"
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    price = models.CharField(max_length=6)
    agency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class Africa(models.Model):
    region = "Africa"
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    price = models.CharField(max_length=6)
    agency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class China(models.Model):
    region = "China"
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    price = models.CharField(max_length=6)
    agency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class America(models.Model):
    region = "America"
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    price = models.CharField(max_length=6)
    agency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

#include West and South Asia
class MiddleAsia(models.Model):
    region = "MiddleAsia"
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    price = models.CharField(max_length=6)
    agency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

class SouthEastAsia(models.Model):
    region = "South East Asia"
    title = models.CharField(max_length=100)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    price = models.CharField(max_length=6)
    agency = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    link = models.URLField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
