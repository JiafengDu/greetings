"""
URLs for greetings.
"""
from django.conf.urls import url
from .views import GreetingsView

urlpatterns = [
    url(
        'greeting', 
        GreetingsView.as_view(),
        name='greetings'
    ),
]
