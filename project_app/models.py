from django.db import models
from django.urls import reverse

# Create your models here.
class Counselor(models.Model):
    name = models.CharField(max_length=100)
    workemail = models.CharField(max_length=200)
    phone = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)