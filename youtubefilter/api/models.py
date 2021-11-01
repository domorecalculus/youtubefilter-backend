from django.db import models
from django.contrib.postgres.fields import ArrayField
from dataclasses import dataclass
from django.contrib.auth.models import User


class Group(models.Model):
    id = models.UUIDField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channels = models.ManyToManyField('Channel', blank=True)

class Channel(models.Model):
    id = models.CharField(max_length=255, default="", unique=True, primary_key=True)
    title = models.CharField(max_length=255, default="")
    description = models.CharField(max_length=1000, default="")
    thumbnail = models.URLField()
    uploads_playlist_id = models.CharField(max_length=100)

# class Video(models.Model):
#     id = models.CharField(max_length=50, unique=True, primary_key=True)
#     title = models.CharField(max_length=100)
#     thumbnail = models.URLField()
#     date_published = models.DateTimeField()
    
