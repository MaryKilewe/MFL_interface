from django.db import models

# Create your models here.


class IPdata(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)


