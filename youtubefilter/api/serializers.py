from typing import overload
from rest_framework import serializers
from .models import Group
import uuid


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', 'channels']
    
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

