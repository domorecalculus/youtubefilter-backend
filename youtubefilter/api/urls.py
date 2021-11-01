from django.urls import path

from .views import GreetingView, GroupView, GroupDetailView, ChannelView, ChannelDetailView, SearchView, VideoView

urlpatterns = [
    path('greeting', GreetingView.as_view()),
    path('groups', GroupView.as_view()),
    path('groups/<str:pk>', GroupDetailView.as_view()),
    path('channels', ChannelView.as_view()),
    path('channels/<str:pk>', ChannelDetailView.as_view()),
    path('channels/search/', SearchView.as_view()),
    path('videos/', VideoView.as_view()),
]
