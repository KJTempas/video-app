from django.shortcuts import render
from .models import Video

from django.contrib import messages #temp messages shown to user
from .forms import VideoForm

# Create your views here.
def home(request):
    app_name = 'Kickboxing Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

def add(request):
    if request.method == 'POST': #when adding a new video
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            new_video_form.save()
            messages.info(request, 'New Video Saved')
        
        else:
            messages.warning(request, 'Check the data entered')
            #display form again so the user can edit
            return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})
#if it's a GET request
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


def video_list(request):
    videos = Video.objects.order_by('name')
    return render(request, 'video_collection/video_list.html', {'videos': videos})
    
