from django.contrib import admin
from .models import Counselor
from .models import Event

# Register your models here.
admin.site.register(Counselor)
admin.site.register(Event)