"""
    Views for the Drivers API.
    This module contains the views for handling driver-related API requests.
"""

from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.utils.pagination import Paginator
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound, ParseError
from users.auth_services import get_hash_password
from .models import Driver
from .serializers import (
    DriverSerializer,
    DriverDetailSerializer
)
from bson import ObjectId
from datetime import datetime

"""
Classe de serialização para os parâmetros de paginação.
"""
class PaginationParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(min_value=1, required=False)
    limit = serializers.IntegerField(min_value=1, max_value=100, required=False, default=50)


@api_view(['GET'])
def list_drivers(request):
    """List alll drivers."""
    serializer = PaginationParamsSerializer(data=request.query_params)
    if serializer.is_valid():
        page = serializer.validated_data.get('page')
        limit = serializer.validated_data.get('limit')

        pagination = Paginator(
            queryset=Driver.objects.all(),
            per_page=limit,
            base_url=reverse('drivers:list_drivers', request=request),
            serializer_class=DriverSerializer
        ).paginate(page)

        pagination = convert_objectids(pagination)
        
        return Response(pagination)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_driver(request):
    """Create a new driver."""
    serializer = DriverDetailSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hashed_password = get_hash_password(password)
        serializer.validated_data['password'] = hashed_password
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    raise serializers.ValidationError(serializer.errors)

@api_view(['GET'])
def get_driver(request, driver_id):
    """Get driver by id"""
    try:
        driver = Driver.objects.get(id=ObjectId(driver_id))
    except Driver.DoesNotExist:
        raise NotFound("Driver not found")
    return Response(DriverSerializer(driver).data)

@api_view(['DELETE'])
def delete_driver(request, driver_id):
    """Delte driver by id"""
    try:
        driver = Driver.objects.get(id=ObjectId(driver_id))
    except Driver.DoesNotExist:
        raise NotFound("Driver not found")
    except Exception as e:
        raise ParseError(f"Error deleting driver: {str(e)}")
    
    driver.deletedAt  = datetime.now()
    driver.isActive = False
    driver.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_driver(request, driver_id):
    """Update driver by id"""
    try:
        driver = Driver.objects.get(id=ObjectId(driver_id))
    except Driver.DoesNotExist:
        raise NotFound("Driver not found")
    except Exception as e:
        raise ParseError(f"Error updating driver: {e}")
    
    serializer = DriverDetailSerializer(driver, data=request.data, partial=True)
    if serializer.is_valid():
        if 'password' in request.data:
            password = request.data.get('password')
            hashed_password = get_hash_password(password)
            serializer.validated_data['password'] = hashed_password
        serializer.save()
        driver_data = convert_objectids(serializer.data)
        return Response(driver_data)
    raise serializers.ValidationError(serializer.errors)

def convert_objectids(data):
    """Convert ObjectId fields in a dictionary to strings."""
    if isinstance(data, dict):
        return {k: convert_objectids(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [convert_objectids(item) for item in data]
    elif isinstance(data, ObjectId):
        return str(data)
    return data