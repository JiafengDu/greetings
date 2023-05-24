"""
Database models for greetings.
"""

from django.db import models

class Greeting(models.Model):
    """User-inputted greetings"""
    class Meta:
        app_label = "greetings"
        
    text = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return "{} at {}".format(self.text, str(self.created_at))