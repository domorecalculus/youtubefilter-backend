from django.db import models
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
# Users
# Groups
# Channels
# Videos?


class Channel(models.Model):
    # ID
    # Name
    # videoIDs
    # thumbnail image
    id = models.CharField(max_length=50, default="", unique=True, primary_key=True)
    name = models.CharField(max_length=50, default="")
    # video_ids = ArrayField(base_field=models.CharField(max_length=50))
