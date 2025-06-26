from rest_framework.reverse import reverse
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
from core.utils.pagination import Paginator


"""
Classe de serialização para os parâmetros de paginação.
"""
class ListVehicleParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(min_value=1, required=False)
    limit = serializers.IntegerField(min_value=1, max_value=100, required=False, default=50)
    status = serializers.ListField(child=serializers.ChoiceField(choices=VehicleStatus.choices), required=False)
    licensePlate = serializers.CharField(max_length=8, required=False)

@api_view(['GET'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def list_vehicles(request):
    """
    GET /vehicles/
    """
    serializer = ListVehicleParamsSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    page = serializer.validated_data.get('page')
    limit = serializer.validated_data.get('limit')
    status = serializer.validated_data.get('status')
    licensePlate = serializer.validated_data.get('licensePlate')

    # Cria um dicionário de filtros
    filters = {}
    if status:
        filters['status__in'] = status
    else:
        filters['status__nin'] = [VehicleStatus.INACTIVE]
    if licensePlate:
        filters['licensePlate__icontains'] = licensePlate

    pagination = Paginator(
        queryset=Vehicle.objects.filter(**filters),
        per_page=limit,
        base_url=reverse('vehicles:list_vehicles', request=request),
        serializer_class=VehicleSerializer
    ).paginate(page)
    return Response(pagination)


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
    raise serializers.ValidationError(serializer.errors)


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

@api_view(['GET'])
def list_vehicle_status(request):
    """
    GET /vehicles/status/
    """
    status_list = [{"value": value, "label": label} for value, label in VehicleStatus.choices]
    return Response(status_list)