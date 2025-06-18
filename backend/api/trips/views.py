
"""
Views for the Trips API.
This module contains the views for handling trip-related API requests.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from bson import ObjectId
from trips.serializers import TripSerializer
from vehicles.models import Vehicle
from trips.models import Trip
from users.authentication import MongoJWTAuthentication


@api_view(['GET'])
def list_trips(request):
    """List all trips."""
    pass


@api_view(['GET'])
def get_trip(request, trip_id):
    """Get trip by id."""
    pass


@api_view(['DELETE'])
def delete_trip(request, trip_id):
    """Delete a trip."""
    pass

@api_view(['POST'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def create_trip(request):
    """Criar viagem."""
    try:
        vehicle_id = ObjectId(request.data['vehicleId'])
        vehicle = Vehicle.objects.get(id=vehicle_id)
    except Vehicle.DoesNotExist:
        raise NotFound('Veículo não encontrado')
    except Exception:
        raise ParseError('ID do veículo inválido')
    
    # Valida os dados da viagem
    serializer = TripSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Cria e adiciona a nova viagem ao veículo
    trip = Trip(**serializer.validated_data)
    vehicle.trips.append(trip)
    vehicle.save()

    return Response(TripSerializer(trip).data, status=status.HTTP_201_CREATED)

# bruno
@api_view(['PUT'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def update_trip(request, trip_id):
    """Atualiza uma viagem específica"""
    try:
        # Busca a viagem específica no veículo
        vehicle = Vehicle.objects.get(trips__id=trip_id)
        trip = vehicle.trips.get(id=trip_id)
    except Vehicle.DoesNotExist:
        raise NotFound('Veículo não encontrado')
    except Trip.DoesNotExist:
        raise NotFound('Viagem não existe neste veículo')
        
    # Valida e aplica atualizações
    serializer = TripSerializer(trip, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    
    # Salva alterações
    for key, value in serializer.validated_data.items():
        setattr(trip, key, value)
    vehicle.save()
    
    return Response(serializer.data)