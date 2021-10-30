from django.urls import path

from .views import GreetingView, GroupView

urlpatterns = [
    path('greeting', GreetingView.as_view()),
    path('groups', GroupView.as_view())
]
