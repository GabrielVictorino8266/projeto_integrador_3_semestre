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
    DriverSerializer
)
from bson import ObjectId
from datetime import datetime

"""
Classe de serialização para os parâmetros de paginação.
"""
class PaginationParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(min_value=1, required=False)
    limit = serializers.IntegerField(min_value=1, max_value=100, required=False, default=50)
    name = serializers.CharField(required=False)


@api_view(['GET'])
def list_drivers(request):
    """List all drivers."""
    serializer = PaginationParamsSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    page = serializer.validated_data.get('page')
    limit = serializer.validated_data.get('limit')
    name = serializer.validated_data.get('name')

    filters = {}
    if name:
        # Using MongoDB/MongoEngine syntax for case-insensitive search
        filters['name__icontains'] = name

    pagination = Paginator(
        queryset=Driver.objects.filter(**filters),
        per_page=limit,
        base_url=reverse('drivers:list_drivers', request=request),
        serializer_class=DriverSerializer
    ).paginate(page)

    pagination = convert_objectids(pagination)

    return Response(pagination)

@api_view(['POST'])
def create_driver(request):
    """
    Create a new driver.
    """
    try:
        serializer = DriverSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        name = request.data.get('name')
        if not isinstance(name, str) or not name.strip():
            return Response({
                'error': 'Invalid name provided'
            }, status=status.HTTP_400_BAD_REQUEST)

        birth_year = request.data.get('birthYear')
        if not birth_year:
            return Response({
                'error': 'Birth year is required'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            birth_year = datetime.strptime(birth_year, '%Y-%m-%d').year
        except ValueError:
            return Response({
                'error': 'Invalid birth year format. Expected YYYY-MM-DD'
            }, status=status.HTTP_400_BAD_REQUEST)

        name = name.strip()
        name_parts = [n.capitalize().strip() for n in name.split(' ') if n]
        initials = ''.join([n[0] for n in name_parts])

        password = f"{initials}{birth_year}"
        hashed_password = get_hash_password(password)
        
        serializer.validated_data['password'] = hashed_password
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    except Exception as e:
        return Response({
            'error': f'An unexpected error occurred: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
    
    serializer = DriverSerializer(driver, data=request.data, partial=True)
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