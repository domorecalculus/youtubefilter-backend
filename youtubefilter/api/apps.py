from django.apps import AppConfig
import os

YOUTUBE_API_KEY = os.environ.get('YOUTUBE_API_KEY')

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
