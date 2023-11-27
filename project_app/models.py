from django.db import models
from django.urls import reverse

# Create your models here.
class Counselor(models.Model):
    name = models.CharField(max_length=100)
    workemail = models.CharField(max_length=200)
    phone = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
    
class Calendar(models.Model):
    STATUS = (
        ('Busy', 'Busy'),
        ('Not Busy', 'Not Busy'),
    )
    
    counselor = models.ForeignKey(Counselor, null=True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.status
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
    
class CalendarInCounselors(models.Model):
    counselors = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    calendars = models.ForeignKey(Counselor, on_delete=models.CASCADE)

class Meta:
    unique_together = ('counselor', 'calendar')