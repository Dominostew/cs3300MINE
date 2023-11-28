from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
     return render(request, 'project_app/home.html')

def counselor(request):
     return render(request, 'project_app/counselor.html', {'counselor':counselor})

def calendar(request):
     return render(request, 'project_app/calendar.html', {'calendar':calendar})

def createCalendar(request): 
     form = CalendarForm(request.POST)
     if request.method == 'POST':
          #print('Printing post:', request.POST)
          form = CalendarForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     return render(request, 'project_app/create_calendar.html', {'form':form})  

def updateCalendar(request, pk):
     calendar = Calendar.objects.get(id=pk)  
     form = CalendarForm(instance=calendar)
     if request.method == 'POST':
          #print('Printing post:', request.POST)
          form = CalendarForm(request.POST, instance=calendar)
          if form.is_valid():
               form.save()
               return redirect('/')
     context = {'form':form}
     return render(request, 'project_app/create_calendar.html', context)

def deleteCalendar(request, pk):
     calendar = Calendar.objects.get(id=pk) 
     context={'item':calendar}
     return render(request, 'project_app/delete_calendar.html', context)

#calendar
def index(request):
     return HttpResponse('hello')