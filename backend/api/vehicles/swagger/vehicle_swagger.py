from drf_yasg.utils import swagger_auto_schema
from mongoengine import ValidationError
from ..serializer import VehicleSerializer

create_vehicle_swagger = swagger_auto_schema(
    method='post',
    operation_id='create_vehicle',
    operation_description='Cria um veículo com os dados informados',
    request_body=VehicleSerializer,
    responses={
        201: VehicleSerializer,
        400: ValidationError,
        401: 'Unauthorized',
    },
    tags=['Vehicle']
)

update_vehicle_swagger = swagger_auto_schema(
    method='put',
    operation_id='update_vehicle',
    operation_description='Atualiza um veículo com os dados informados',
    request_body=VehicleSerializer,
    responses={
        200: VehicleSerializer,
        400: ValidationError,
        401: 'Unauthorized',
    },
    tags=['Vehicle']
)

delete_vehicle_swagger = swagger_auto_schema(
    method='delete',
    operation_id='delete_vehicle',
    operation_description='Deleta um veículo',
    responses={
        204: 'No Content',
        400: ValidationError,
        401: 'Unauthorized',
    },
    tags=['Vehicle']
)

list_vehicles_swagger = swagger_auto_schema(
    method='get',
    operation_id='list_vehicles',
    operation_description='Lista todos os veículos',
    responses={
        200: VehicleSerializer(many=True),
        400: ValidationError,
        401: 'Unauthorized',
    },
    tags=['Vehicle']
)

get_vehicle_swagger = swagger_auto_schema(
    method='get',
    operation_id='get_vehicle',
    operation_description='Obtém um veículo pelo ID',
    responses={
        200: VehicleSerializer,
        400: ValidationError,
        401: 'Unauthorized',
    },
    tags=['Vehicle']
)
