from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
     return render(request, 'project_app/home.html')

def counselor(request):
     return render(request, 'project_app/counselor.html', {'counselor':counselor})

def event(request):
     return render(request, 'project_app/event.html', {'event':event})

def createEvent(request): 
     form = CalendarForm(request.POST)
     if request.method == 'POST':
          form = CalendarForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect('/')
     return render(request, 'project_app/create_event.html', {'form':form})  

def updateEvent(request, pk):
     event = Event.objects.get(id=pk)  
     form = CalendarForm(instance=event)
     if request.method == 'POST':
          #print('Printing post:', request.POST)
          form = CalendarForm(request.POST, instance=event)
          if form.is_valid():
               form.save()
               return redirect('/')
     return render(request, 'project_app/create_event.html', {'form':form})

def deleteEvent(request, pk):
     event = Event.objects.get(id=pk) 
     return render(request, 'project_app/delete_event.html', {'item':event})