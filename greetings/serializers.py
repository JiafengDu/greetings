"""
Serializers for Greetings
"""

from rest_framework import serializers
from .models import Greeting

class GreetingSerializer(serializers.ModelSerializer):
    """
    Serializer for Greeting model
    """
    class Meta:
        """ Serializer metadata """
        model = Greeting
        fields = (
            'text',
            'created_at',
        )