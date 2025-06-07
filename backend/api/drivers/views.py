"""
    Views for the Drivers API.
    This module contains the views for handling driver-related API requests.
"""

from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.utils.pagination import Paginator
from rest_framework import serializers
from rest_framework import status
from mongoengine import QuerySet
from django.http import Http404
from .models import Driver
from .serializers import (
    DriverSerializer
)

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
