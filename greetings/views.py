"""
Views to capture greetings
"""

import logging
import eventtracking

from django.conf import settings
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication

from edx_rest_api_client.client import OAuthAPIClient

from .serializers import GreetingSerializer
from .models import Greeting

log = logging.getLogger(__name__)

class GreetingsView(ListCreateAPIView):
    """REST endpoint for list of Greetings and creating new Greetings"""
    
    authentication_classes = (JwtAuthentication, SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = GreetingSerializer
    queryset = Greeting.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        if serializer.data['text'] == "hello":
            client = OAuthAPIClient(
                "http://local.overhang.io:8000/oauth2/access_token",
                "4SDIj9f6XTllR2qnnUsDBu84Y6VsLiwe0OWy0h02",
                "krLS5Oj2stIpWR8durgBkJO7BAef7Dk43MjCqluNyQsQ0S9pU5qFHDfmOC8QA3esBlzRplk4wro64ONmRQXoAZFYas2fhPbdlUkVOVQvQ3MjcyrQ46h73P4g6RApc33G",
            )
            data = {"text": "goodbye"}
            res = client.post("http://local.overhang.io:8000/api/greeting", data = data)
            res.raise_for_status()
            return Response(res.json(), status=status.HTTP_201_CREATED)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)