from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from trips.serializers import TripSerializer, TripListParamsSerializer, TripListSerializerById
from rest_framework import serializers
from bson import ObjectId

# Define schemas de resposta de erro
error_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'detail': openapi.Schema(type=openapi.TYPE_STRING, description='Mensagem de erro'),
    }
)

validation_error_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'field_name': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING),
            description='Erros de validação do campo'
        ),
        'non_field_errors': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING),
            description='Erros gerais de validação'
        ),
    }
)

class CreateTripSerializer(TripSerializer):
    vehicleId = serializers.CharField(required=True, help_text="ID do veículo")

# List Trips
list_trips_swagger = swagger_auto_schema(
    method='get',
    operation_id='list_trips',
    operation_summary='Lista todas as viagens',
    operation_description='Lista todas as viagens com suporte a paginação e filtros',
    query_serializer=TripListParamsSerializer(),
    responses={
        200: openapi.Response(
            description='Lista de viagens retornada com sucesso',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'total': openapi.Schema(type=openapi.TYPE_INTEGER, description='Total de viagens encontradas'),
                    'page': openapi.Schema(type=openapi.TYPE_INTEGER, description='Página atual'),
                    'pages': openapi.Schema(type=openapi.TYPE_INTEGER, description='Total de páginas'),
                    'limit': openapi.Schema(type=openapi.TYPE_INTEGER, description='Itens por página'),
                    'items': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Items(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_STRING, format='uuid'),
                                'driverId': openapi.Schema(type=openapi.TYPE_STRING, format='uuid'),
                                'driverName': openapi.Schema(type=openapi.TYPE_STRING),
                                'startDateTime': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                                'endDateTime': openapi.Schema(type=openapi.TYPE_STRING, format='date-time'),
                                'origin': openapi.Schema(type=openapi.TYPE_STRING),
                                'destination': openapi.Schema(type=openapi.TYPE_STRING),
                                'initialKm': openapi.Schema(type=openapi.TYPE_NUMBER, format='float'),
                                'finalKm': openapi.Schema(type=openapi.TYPE_NUMBER, format='float'),
                                'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                                'status': openapi.Schema(type=openapi.TYPE_STRING)
                            }
                        )
                    )
                }
            )
        ),
        400: openapi.Response(description='Parâmetros inválidos', schema=error_response_schema),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema)
    },
    tags=['Trips'],
    security=[{'Bearer': []}]
)

# Get Trip by ID
get_trip_swagger = swagger_auto_schema(
    method='get',
    operation_id='get_trip',
    operation_summary='Obtém uma viagem pelo ID',
    operation_description='Retorna os detalhes de uma viagem específica',
    responses={
        200: openapi.Response(
            description='Viagem retornada com sucesso',
            schema=TripListSerializerById()
        ),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
        404: openapi.Response(description='Viagem não encontrada', schema=error_response_schema)
    },
    tags=['Trips'],
    security=[{'Bearer': []}],
    manual_parameters=[
        openapi.Parameter(
            'id',
            openapi.IN_PATH,
            description='ID da viagem',
            type=openapi.TYPE_STRING,
            required=True
        )
    ]
)

# Delete Trip
delete_trip_swagger = swagger_auto_schema(
    method='delete',
    operation_id='delete_trip',
    operation_summary='Remove uma viagem',
    operation_description='Remove uma viagem específica (soft delete)',
    responses={
        200: openapi.Response(
            description='Viagem removida com sucesso',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING)
                }
            )
        ),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
        404: openapi.Response(description='Viagem não encontrada', schema=error_response_schema),
        400: openapi.Response(description='Erro ao processar a requisição', schema=error_response_schema)
    },
    tags=['Trips'],
    security=[{'Bearer': []}],
    manual_parameters=[
        openapi.Parameter(
            'id',
            openapi.IN_PATH,
            description='ID da viagem a ser removida',
            type=openapi.TYPE_STRING,
            required=True
        )
    ]
)

# Create Trip
create_trip_swagger = swagger_auto_schema(
    method="post",
    operation_id='create_trip',
    operation_summary='Criação de viagem',
    operation_description='Cria uma nova viagem associada a um veículo',
    request_body=CreateTripSerializer(),
    responses={
        201: openapi.Response(description='Viagem criada com sucesso'),
        400: openapi.Response(description='Dados inválidos', schema=validation_error_schema),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
        404: openapi.Response(description='Veículo não encontrado', schema=error_response_schema),
    },
    tags=['Trips'],
    security=[{'Bearer': []}]
)

# Update Trip
update_trip_swagger = swagger_auto_schema(
    method="put",
    operation_id='update_trip',
    operation_summary='Atualização de viagem',
    operation_description='Atualiza os dados de uma viagem existente',
    request_body=TripSerializer(partial=True),
    responses={
        200: openapi.Response(description='Viagem atualizada com sucesso'),
        400: openapi.Response(description='Dados inválidos', schema=validation_error_schema),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
        404: openapi.Response(description='Viagem não encontrada', schema=error_response_schema),
    },
    tags=['Trips'],
    security=[{'Bearer': []}],
    manual_parameters=[
        openapi.Parameter(
            'id',
            openapi.IN_PATH,
            description='ID da viagem a ser atualizada',
            type=openapi.TYPE_STRING,
            required=True
        )
    ]
)
