from django.urls import path
from . import views
#these are the urls for our app

urlpatterns =[
    path('', views.home, name='home'), #empty string means the home page
    path('add', views.add, name='add_video'),
    path('video_list', views.video_list, name='video_list'),
    path('video/<int:video_pk>', views.video_detail, name='video_detail'),
    path('video/<int:video_pk>/delete', views.delete_video, name='delete_video')
]