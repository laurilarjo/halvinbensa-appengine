from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.name

class Station(models.Model):
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    company = models.ForeignKey(Company, related_name='stations')
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    
    def __unicode__(self):
        return self.title
    
class Price(models.Model):
    station = models.ForeignKey(Station, related_name='prices')
    type = models.CharField(max_length=20)
    updated = models.DateTimeField()
    price = models.DecimalField(max_digits=5, decimal_places=3)
    
    def __unicode__(self):
        return '%s %s' % (self.station, self.type)
    