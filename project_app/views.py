from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
     return render(request, 'project_app/home.html')

def counselor(request):
     return render(request, 'project_app/counselor.html', {'counselor':counselor})

def calendar(request):
     return render(request, 'project_app/calendar.html', {'calendar':calendar})