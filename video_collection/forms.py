from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'url', 'notes']


class SearchForm(forms.Form): #basic django form; not related to a model
    search_term =forms.CharField()


        