from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework.response import Response
from django.http import HttpResponse
import requests
from .apps import YOUTUBE_API_KEY
from .serializers import ChannelSerializer, GroupSerializer
from .models import Channel, Group

class GreetingView(APIView):
    def get(self, request, format=None):
        return HttpResponse('Hello there')

class GroupView(generics.ListCreateAPIView):
    serializer_class = GroupSerializer
    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)
    

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    def get_queryset(self):
        return Group.objects.filter(user=self.request.user)

class ChannelView(generics.ListCreateAPIView):
    serializer_class = ChannelSerializer
    def get_queryset(self):
        return Channel.objects.filter(pk__in=self.request.query_params.getlist('ids', ''))
    
class ChannelDetailView(generics.RetrieveAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    
class SearchView(APIView):
    def get(self, request):
        q = request.query_params.get('q', '')
        url = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&order=relevance&q=" + q + "&type=channel&key=" + YOUTUBE_API_KEY
        res = requests.get(url)
        return HttpResponse(res)

class VideoView(APIView):
    def get(self, request):
        list_ids = request.query_params.getlist('ids', '')
        videos = []
        for id in list_ids:
            url = "https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=" + id + "&key=" + YOUTUBE_API_KEY
            res = requests.get(url)
            for video in res.json()['items']:
                videos.append(video)

        return Response(videos)
