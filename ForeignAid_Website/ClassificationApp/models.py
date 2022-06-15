from django.db import models

# Create your models here.

class CountryData(models.Model):
    aggriculture  = models.FloatField()
    industry      = models.FloatField()
    manufacturing = models.FloatField()
    services      = models.FloatField()

'''
class CountryClass(models.Model):
    country_code = models.CharField()
    country_name = models.CharField()
    country_class = models.FloatField()
    '''
