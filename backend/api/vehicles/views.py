from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from bson import ObjectId

from .models import Vehicle
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
    return Response(serializer.data, status=status.HTTP_200_OK)


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
        return Response({'detail': 'Veículo não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'detail': 'ID inválido'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = VehicleSerializer(vehicle)
    return Response(serializer.data, status=status.HTTP_200_OK)


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
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        return Response({'detail': 'Veículo não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'detail': 'ID inválido'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = VehicleSerializer(vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        return Response({'detail': 'Veículo não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return Response({'detail': 'ID inválido'}, status=status.HTTP_400_BAD_REQUEST)

    vehicle.delete()
    return Response({'detail': 'Veículo deletado com sucesso'}, status=status.HTTP_204_NO_CONTENT)