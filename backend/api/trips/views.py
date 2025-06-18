
"""
Views for the Trips API.
This module contains the views for handling trip-related API requests.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, ParseError
from bson import ObjectId
from trips.serializers import TripSerializer
from vehicles.models import Vehicle

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
def create_trip(request):
    """Criar viagem."""
    try:
        vehicle_id = ObjectId(request.data['vehicleId'])
    except Exception:
        raise ParseError('ID do veículo inválido')
    
    serializer = TripSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    # Utilizar operação atômica de push
    result = Vehicle.objects(id=vehicle_id).update_one(
        push__trips=serializer.validated_data
    )
    
    if result == 0:
        raise NotFound('Veículo não encontrado')
    
    # Obter o veículo para retornar a viagem recém-criada
    vehicle = Vehicle.objects.get(id=vehicle_id)
    new_trip = vehicle.trips[-1]  # Last added trip
    
    return Response(TripSerializer(new_trip).data, status=status.HTTP_201_CREATED)

# bruno
@api_view(['PUT', 'PATCH'])
def update_trip(request, trip_id):
    """Atualizar viagem."""
    try:
        vehicle = Vehicle.objects.get(id=ObjectId(request.data['vehicleId']))
    except Vehicle.DoesNotExist:
        raise NotFound('Veículo não encontrado')
    except Exception:
        raise ParseError('ID do veículo inválido')
    
    try:
        trip = vehicle.trips.get(id=ObjectId(trip_id))
    except Trip.DoesNotExist:
        raise NotFound('Viagem não encontrada')
    except Exception:
        raise ParseError('ID da viagem inválido')

    serializer = TripSerializer(trip, data=request.data)
    serializer.is_valid(raise_exception=True)
    
    trip.update(**serializer.validated_data)
    vehicle.save()
    return Response(serializer.data)