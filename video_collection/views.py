from django.shortcuts import render, redirect,get_object_or_404
from .models import Video

from django.contrib import messages #temp messages shown to user
from .forms import VideoForm, SearchForm

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.db.models.functions import Lower
from django.http import HttpResponseForbidden
#Lower helps sort everything case insensitive in lower case

# Create your views here.
def home(request):
    app_name = 'Kickboxing Videos'
    return render(request, 'video_collection/home.html', {'app_name': app_name})

def add(request):
    if request.method == 'POST': #when adding a new video
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:
                new_video_form.save()
                return redirect('video_list')
        
            except ValidationError:
                messages.warning(request, 'Invalid YouTube URL')
            except IntegrityError: #caused by duplicate video ID
                messages.warning(request, 'You already added that video')

        
        messages.warning(request, 'Check the data entered')
        #display form again so the user can edit
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})
#if it's a GET request
    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


def video_list(request):

    search_form = SearchForm(request.GET) #build form out of info user submitted

    if search_form.is_valid():
        search_term = search_form.cleaned_data['search_term'] 
                        #searches case insensitive 
        videos = Video.objects.filter(name__icontains=search_term).order_by(Lower('name'))

    else: #form is not filled in 
        search_form = SearchForm() #make a new search form
        videos = Video.objects.order_by(Lower('name')) #get all the videos

    return render(request, 'video_collection/video_list.html', {'videos': videos, 'search_form': search_form})

    #@login_required
def video_detail(request, video_pk):
    #retrieve the video with the pk provided
    video = get_object_or_404(Video, pk=video_pk)
    #login is not required for this app, so don't check if video.user = request.user

    #render the template
    return render(request, 'video_collection/video_detail.html', {'video': video} )

    
