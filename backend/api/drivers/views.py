"""
    Views for the Drivers API.
    This module contains the views for handling driver-related API requests.
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import Http404

from .serializers import (
    DriverSerializer,
    DriverCreateSerializer,
    DriverUpdateSerializer,
    DriverDeleteSerializer,
)

from .services import DriverService as driverservice
from .models import Driver

"""
    Main ViewSet
"""

class DriverViewSet(viewsets.ViewSet):
    """
    ViewSet for handling driver-related API requests.
    - GET    /motoristas/           → list()
    - POST   /motoristas/           → create()  
    - GET    /motoristas/{id}/      → retrieve()
    - PUT    /motoristas/{id}/      → update()
    - DELETE /motoristas/{id}/      → destroy()
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = driverservice

    def list(self, request):
        """
            List all drivers.
            Methods:
                GET - /drives/
                GET - /drivers/?name={name}
        """
        filters = self._extract_filtes(request.query_params)
        try:
            drivers = self.service.get_all(filters)
            drivers_data = [driver.to_dict() for driver in drivers]
            serializer = DriverSerializer(drivers_data, many=True)
            
            return Response({
                'success': True,
                'count': len(drivers_data),
                'results': serializer.data
            })
        
        except ValueError as e:
            return Response({'error': str(e)}, status=400)
        
        except ConnectionError as e:
            return Response({'error': 'Connection Error'}, status=503)

    def _extract_filtes(self, query_params):
        """
            Extract filters from query parameters.
        """
        filters = {}
        if query_params.get('name'):
            filters['name'] = query_params.get('name')

        return filters