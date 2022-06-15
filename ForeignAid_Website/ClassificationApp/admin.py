from django.contrib import admin
from .models import CountryData

# Register your models here.
# this makes them show up in the Django admin site

admin.site.register(CountryData)
