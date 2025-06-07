"""
    Views for the Drivers API.
    This module contains the views for handling driver-related API requests.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Driver
from .serializers import (
    DriverSerializer
)
from bson import ObjectId
from .driver_services import DriverService

@api_view(['GET'])
def list_drivers(request):
    """List alll drivers."""
    try:
        service = DriverService()
        drivers = service.get_all_drivers(request.GET)
        serializer = DriverSerializer(drivers, many=True)

        return Response({
            'success': True,
            'message': 'Lista de Motoristas',
            'data': serializer.data
        })
    except Exception as e:
        return Response({
            'sucess': False,
            'message': f'Falha ao listar motoristas: {e}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)