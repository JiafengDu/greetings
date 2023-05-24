"""
Admin registration for Greeting
"""

from django.contrib import admin

from .models import Greeting

@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    pass
