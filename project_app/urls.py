from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('counselor/', views.counselor, name='counselor'),
     path('event/', views.event, name='event'),
     
     path('create_event/', views.createEvent, name='create_event'), 
     path('update_event/<str:pk>/', views.updateEvent, name='update_event'),
     path('delete_event/<str:pk>/', views.deleteEvent, name='delete_event'),
]