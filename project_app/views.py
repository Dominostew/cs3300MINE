from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
     return render(request, 'project_app/home.html')

def user(request):
     return render(request, 'project_app/user.html')