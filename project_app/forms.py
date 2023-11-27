from django.forms import ModelForm
from .models import *

class CalendarForm(ModelForm):
    class Meta:
        model = Calendar
        fields = '__all__'