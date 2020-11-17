from django.db import models

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        #string displays in the admin console, or when printing a model object
        #note that note info is limited in size
        return f'ID: {self.pk}, Name: {self.name}, URL: {self.url}, Notes: {self.notes[:200]}'