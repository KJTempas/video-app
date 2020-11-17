from django.urls import path
from . import views
#these are the urls for our app

urlpatterns =[
    path('', views.home, name='home'), #empty string means the home page
    path('add', views.add, name='add_video')
]