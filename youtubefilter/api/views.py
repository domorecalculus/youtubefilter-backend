from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse

class GreetingView(APIView):
    def get(self, request, format=None):
            return HttpResponse('Hello there')