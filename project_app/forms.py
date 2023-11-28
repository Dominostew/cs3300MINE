from django.forms import ModelForm
from .models import *

class CalendarForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'