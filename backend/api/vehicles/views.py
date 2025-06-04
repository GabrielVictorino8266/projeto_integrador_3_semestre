from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.response import Response
from bson import ObjectId
import datetime

from .models import Vehicle
from .types import VehicleStatus
from .serializer import VehicleSerializer
from users.authentication import MongoJWTAuthentication
from .swagger.vehicle_swagger import (
    create_vehicle_swagger,
    update_vehicle_swagger,
    delete_vehicle_swagger,
    list_vehicles_swagger,
    get_vehicle_swagger
)

@list_vehicles_swagger
@api_view(['GET'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def list_vehicles(request):
    """
    GET /vehicles/
    """
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@get_vehicle_swagger
@api_view(['GET'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def get_vehicle(request, id):
    """
    GET /vehicles/<id>/
    """
    try:
        vehicle = Vehicle.objects.get(id=ObjectId(id))
    except Vehicle.DoesNotExist:
        raise NotFound('Veículo não encontrado')
    except Exception:
        raise ParseError('ID inválido')

    serializer = VehicleSerializer(vehicle)
    return Response(serializer.data)


@create_vehicle_swagger
@api_view(['POST'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def create_vehicle(request):
    """
    POST /vehicles/create/
    """
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    raise serializers.ValidationError(serializer.errors)


@update_vehicle_swagger
@api_view(['PUT'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def update_vehicle(request, id):
    """
    PUT /vehicles/update/<id>/
    """
    try:
        vehicle = Vehicle.objects.get(id=ObjectId(id))
    except Vehicle.DoesNotExist:
        raise NotFound('Veículo não encontrado')
    except Exception:
        raise ParseError('ID inválido')

    serializer = VehicleSerializer(vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    raise ParseError(serializer.errors)


@delete_vehicle_swagger
@api_view(['DELETE'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_vehicle(request, id):
    """
    DELETE /vehicles/delete/<id>/
    """
    try:
        vehicle = Vehicle.objects.get(id=ObjectId(id))
    except Vehicle.DoesNotExist:
        raise NotFound('Veículo não encontrado')
    except Exception:
        raise ParseError('ID inválido')

    vehicle.deletedAt = datetime.datetime.now()
    vehicle.status = VehicleStatus.INACTIVE
    vehicle.save()
    return Response('Veículo deletado com sucesso', status=status.HTTP_204_NO_CONTENT)
