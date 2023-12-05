from django.urls import path, include
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('counselor/', views.counselor, name='counselor'),
     path('event/', views.event, name='event'),

     path('accounts/login', views.loginPage, name='login'),
     path('accounts/register', views.registerPage, name='register'),
]