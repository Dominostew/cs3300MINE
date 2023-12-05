from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def home(request):
     return render(request, 'project_app/home.html')

def counselor(request):
     return render(request, 'project_app/counselor.html', {'counselor':counselor})

def event(request):
     return render(request, 'project_app/event.html', {'event':event})

def registerPage(request):
     form = CreateUserForm()

     if request.method == 'POST':
          form = CreateUserForm(request.POST)
          if form.is_valid():
               user = form.save()
               username = form.cleaned_data.get('username')
               
               messages.success(request, 'Account was created for' + username)
               return redirect('login')

     return render(request, 'accounts/register.html', {'form':form})

def loginPage(request):
     return render(request, 'accounts/login.html', {})