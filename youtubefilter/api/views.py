from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpResponse

from .serializers import GroupSerializer
from .models import Group

class GreetingView(APIView):
    def get(self, request, format=None):
        return HttpResponse('Hello there')

class GroupView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    # def perform_create(self, serializer):
        # serializer.save(user=self.request.user)