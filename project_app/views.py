from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     return render(request, 'project_app/home.html')

def user(request):
     return HttpResponse('user')

def calendar(request):
     return HttpResponse('calendar')