
"""
Views for the Trips API.
This module contains the views for handling trip-related API requests.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, ParseError
from bson import ObjectId

# from .models import Trip
# from .serializers import TripSerializer

@api_view(['GET'])
def list_trips(request):
    """List all trips."""
    pass

@api_view(['POST'])
def create_trip(request):
    """Create a new trip."""
    pass

@api_view(['GET'])
def get_trip(request, trip_id):
    """Get trip by id."""
    pass

@api_view(['DELETE'])
def delete_trip(request, trip_id):
    """Delete a trip."""
    pass

@api_view(['PUT', 'PATCH'])
def update_trip(request, trip_id):
    """Update a trip."""
    pass