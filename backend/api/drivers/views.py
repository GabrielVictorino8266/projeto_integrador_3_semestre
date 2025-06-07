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

        return Response(pagination)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_driver(request):
    """Create a new driver."""
    serializer = DriverSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')
        hashed_password = get_hash_password(password)
        serializer.validated_data['password'] = hashed_password
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    raise serializers.ValidationError(serializer.errors)