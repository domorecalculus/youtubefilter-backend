from django.db import models
from django.contrib.postgres.fields import ArrayField
from dataclasses import dataclass
from django.contrib.auth.models import User


# Create your models here.

class Group(models.Model):
    id = models.UUIDField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channels = models.ManyToManyField('Channel')

class Channel(models.Model):
    id = models.CharField(max_length=255, default="", unique=True, primary_key=True)
    name = models.CharField(max_length=255, default="")
    video_ids = ArrayField(base_field=models.CharField(max_length=50))
    thumbnail = models.URLField()
