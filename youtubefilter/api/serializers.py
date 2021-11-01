from typing import overload

import requests
from rest_framework import serializers
from .apps import YOUTUBE_API_KEY
from .models import Channel, Group
import uuid


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'channels']
        extra_kwargs = {'id': {'read_only': True}}
    
    def validate(self, data):
        if 'name' not in data:
            raise serializers.ValidationError("'name' is a required field")
        return data
    
    def create(self, validated_data):
        print(validated_data)
        user = self.context['request'].user
        print(user)
        group = Group.objects.create(id=uuid.uuid4(), name=validated_data['name'], user=user)
        print(group)
        group.save()
        return group
        
class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title', 'description', 'thumbnail', 'uploads_playlist_id']
        extra_kwargs = {'uploads_playlist_id': {'read_only': True}}
        
    def create(self, validated_data):
        url = "https://www.googleapis.com/youtube/v3/channels?part=snippet&part=contentDetails&id=" + validated_data['id'] + "&key=" + YOUTUBE_API_KEY
        res = requests.get(url)
        print(res.json())
        #get uploads playlist id
        uploads_playlist_id = res.json()['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        #create channel
        channel = Channel.objects.create(**validated_data, uploads_playlist_id=uploads_playlist_id)
        channel.save()
        return channel
    

