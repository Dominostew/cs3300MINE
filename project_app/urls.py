from django.urls import path
from . import views

#calendar
from django.conf.urls import url

app_name = 'project_app'
urlpatterns = [
     path('', views.home, name='home'),
     path('counselor/', views.counselor, name='counselor'),
     path('calendar/', views.calendar, name='calendar'),
     
     path('create_calendar/', views.createCalendar, name='create_calendar'), 
     path('update_calendar/<str:pk>/', views.updateCalendar, name='update_caledar'),
     path('delete_calendar/<str:pk>/', views.deleteCalendar, name='delete_caledar'),

     #calendar
     url(r'^index/$', views.index, name='index'),
]