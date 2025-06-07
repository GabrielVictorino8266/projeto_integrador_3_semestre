"""
    Serializers for the Drivers API.
    This module contains the serializers for handling driver-related API requests.
"""

from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Driver

class DriverSerializer(DocumentSerializer):
    class Meta:
        model = Driver
        fields = '__all__'