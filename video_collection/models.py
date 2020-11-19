from urllib import parse #allows you to pull out parts of a url
from django.db import models
from django.core.exceptions import ValidationError 

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null=True)
    video_id = models.CharField(max_length=40, unique=True)

    def save(self, *args, **kwargs): #key word arguments = kwargs
        #checks for a valid YouTube URL in the form
        #video ID isdigits after v= in URL
        #extract videoID from URL, prevent save if not valid URL or ID not found in URL
        try:
            url_components = parse.urlparse(self.url)
            if url_components.scheme !='https' or url_components.netloc != 'www.youtube.com' or url_components.path != '/watch':
                raise ValidationError(f'Invalid YouTube URL {self.url}')
            #pullingout the querry string, the v=
            query_string = url_components.query #everything after the ? in the url
            if not query_string:
                raise ValidationError(f'Invalid YouTube URL {self.url}')
            parameters = parse.parse_qs(query_string, strict_parsing=True) #convert v = 1234 to a dictionary v: 1234
            parameter_list = parameters.get('v') #dictionary - key = v; value = the video ID; if no v - returns None
            if not parameter_list:  #if an empty string, empty list
                raise ValidationError(f'Invalid YouTube URL, missing parameters {self.url}')
            self.video_id = parameter_list[0] #set videoID for this video object; the string
        
        except ValueError as e: #URL parsing errors, malformed URLs
            raise ValidationError(f'Unable to parse URL {self.url}') from e

        super().save(*args, **kwargs)  #save to dbase after runnign this this overrides normal save method


    def __str__(self):
        #string displays in the admin console, or when printing a model object
        #note that note info is limited in size
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Video ID: {self.video_id},  Notes: {self.notes[:200]}'