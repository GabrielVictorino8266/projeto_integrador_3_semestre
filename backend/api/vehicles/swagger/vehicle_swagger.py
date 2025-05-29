from drf_yasg.utils import swagger_auto_schema
from .serializer import VehicleSerializer

create_vehicle_swagger = swagger_auto_schema(
    operation_id='create_vehicle',
    operation_description='Cria um veículo com os dados informados',
    request_body=VehicleSerializer,
    responses={
        201: VehicleSerializer,
        400: 'Parâmetros inválidos',
    }
)

update_vehicle_swagger = swagger_auto_schema(
    operation_id='update_vehicle',
    operation_description='Atualiza um veículo com os dados informados',
    request_body=VehicleSerializer,
    responses={
        200: VehicleSerializer,
        400: 'Parâmetros inválidos',
    }
)

delete_vehicle_swagger = swagger_auto_schema(
    operation_id='delete_vehicle',
    operation_description='Deleta um veículo',
    responses={
        204: 'No Content',
        400: 'Parâmetros inválidos',
    }
)

list_vehicles_swagger = swagger_auto_schema(
    operation_id='list_vehicles',
    operation_description='Lista todos os veículos',
    responses={
        200: VehicleSerializer(many=True),
        400: 'Erro ao buscar veículos',
    }
)

get_vehicle_swagger = swagger_auto_schema(
    operation_id='get_vehicle',
    operation_description='Obtém um veículo pelo ID',
    responses={
        200: VehicleSerializer,
        400: 'Parâmetros inválidos',
    }
)
