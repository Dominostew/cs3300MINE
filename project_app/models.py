from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):

    CITY = (
        ('COSPRGS', 'Colorado Springs'),
        ('DEN', 'Denver'),
        ('PBLO' ,'Pueblo'),
        ('NRGLN', 'Northglenn'),
        ('LNGMT', 'Longmont'),
        ('MONT', 'Montrose'),
    )

    name = models.CharField(max_length=100)
    workemail = models.CharField("Work Email", max_length=200)
    city = models.CharField(max_length=100, choices=CITY, blank = True)