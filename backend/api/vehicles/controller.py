from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from users.authentication import MongoJWTAuthentication
from .swagger.vehicle_swagger import (
    create_vehicle_swagger,
    update_vehicle_swagger,
    delete_vehicle_swagger,
    list_vehicles_swagger,
    get_vehicle_swagger
)

@create_vehicle_swagger
@api_view(['POST'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def create_vehicle(request):
    pass

@update_vehicle_swagger
@api_view(['PUT'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def update_vehicle(request):
    pass

@delete_vehicle_swagger
@api_view(['DELETE'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_vehicle(request):
    pass

@list_vehicles_swagger
@api_view(['GET'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def list_vehicles(request):
    pass

@get_vehicle_swagger
@api_view(['GET'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def get_vehicle(request):
    pass