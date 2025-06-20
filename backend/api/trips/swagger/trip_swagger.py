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
    operation_description='Lista todas as viagens com suporte a paginação e filtros. As viagens são ordenadas por data de criação (mais recentes primeiro).',
    manual_parameters=[
        openapi.Parameter(
            'page', 
            openapi.IN_QUERY, 
            description='Número da página (padrão: 1)', 
            type=openapi.TYPE_INTEGER,
            default=1,
            required=False
        ),
        openapi.Parameter(
            'limit', 
            openapi.IN_QUERY, 
            description='Número de itens por página (padrão: 10, máximo: 100)', 
            type=openapi.TYPE_INTEGER,
            default=10,
            required=False
        ),
        openapi.Parameter(
            'destination', 
            openapi.IN_QUERY, 
            description='Filtrar por destino (busca parcial, case insensitive)', 
            type=openapi.TYPE_STRING,
            required=False
        ),
        openapi.Parameter(
            'status', 
            openapi.IN_QUERY, 
            description=f'Filtrar por status. Valores possíveis: active, cancelled, in_progress', 
            type=openapi.TYPE_STRING,
            required=False
        ),
    ],
    responses={
        200: openapi.Response(
            description='Lista de viagens retornada com sucesso',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'total': openapi.Schema(type=openapi.TYPE_INTEGER, description='Total de itens'),
                    'per_page': openapi.Schema(type=openapi.TYPE_INTEGER, description='Itens por página'),
                    'current_page': openapi.Schema(type=openapi.TYPE_INTEGER, description='Página atual'),
                    'last_page': openapi.Schema(type=openapi.TYPE_INTEGER, description='Última página'),
                    'first_page_url': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description='URL da primeira página'),
                    'last_page_url': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description='URL da última página'),
                    'next_page_url': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description='URL da próxima página', nullable=True),
                    'prev_page_url': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description='URL da página anterior', nullable=True),
                    'path': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description='Caminho base da requisição'),
                    'from': openapi.Schema(type=openapi.TYPE_INTEGER, description='Número do primeiro item da página'),
                    'to': openapi.Schema(type=openapi.TYPE_INTEGER, description='Número do último item da página'),
                    'items': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=openapi.Items(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_STRING, description='ID único da viagem'),
                                'driverId': openapi.Schema(type=openapi.TYPE_STRING, description='ID do motorista'),
                                'driverName': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do motorista', nullable=True),
                                'startDateTime': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Data e hora de início da viagem'),
                                'endDateTime': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Data e hora de término da viagem', nullable=True),
                                'origin': openapi.Schema(type=openapi.TYPE_STRING, description='Local de origem'),
                                'destination': openapi.Schema(type=openapi.TYPE_STRING, description='Local de destino'),
                                'initialKm': openapi.Schema(type=openapi.TYPE_NUMBER, description='Quilometragem inicial'),
                                'finalKm': openapi.Schema(type=openapi.TYPE_NUMBER, description='Quilometragem final', nullable=True),
                                'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Indica se a viagem foi concluída'),
                                'status': openapi.Schema(type=openapi.TYPE_STRING, enum=['active', 'cancelled', 'in_progress'], description='Status da viagem'),
                                'createdAt': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Data de criação'),
                                'updatedAt': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Data da última atualização')
                            }
                        )
                    )
                }
            )
        ),
        400: openapi.Response(description='Parâmetros inválidos', schema=error_response_schema),
        401: openapi.Response(description='Não autenticado', schema=error_response_schema),
        403: openapi.Response(description='Não autorizado', schema=error_response_schema)
    },
    tags=['Trips'],
    security=[{'Bearer': []}]
)

# Get Trip by ID
get_trip_swagger = swagger_auto_schema(
    method='get',
    operation_id='get_trip',
    operation_summary='Obtém uma viagem pelo ID',
    operation_description='Retorna os detalhes de uma viagem específica pelo seu ID',
    responses={
        200: openapi.Response(
            description='Detalhes da viagem',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_STRING, description='ID único da viagem'),
                    'driverName': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do motorista', nullable=True),
                    'startDateTime': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Data e hora de início da viagem'),
                    'origin': openapi.Schema(type=openapi.TYPE_STRING, description='Local de origem'),
                    'destination': openapi.Schema(type=openapi.TYPE_STRING, description='Local de destino'),
                    'initialKm': openapi.Schema(type=openapi.TYPE_NUMBER, description='Quilometragem inicial'),
                    'finalKm': openapi.Schema(type=openapi.TYPE_NUMBER, description='Quilometragem final', nullable=True),
                    'completed': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Indica se a viagem foi concluída'),
                    'status': openapi.Schema(type=openapi.TYPE_STRING, enum=['active', 'cancelled', 'in_progress'], description='Status da viagem')
                }
            )
        ),
        400: openapi.Response(description='ID inválido', schema=error_response_schema),
        401: openapi.Response(description='Não autenticado', schema=error_response_schema),
        403: openapi.Response(description='Não autorizado', schema=error_response_schema),
        404: openapi.Response(description='Viagem não encontrada', schema=error_response_schema)
    },
    tags=['Trips'],
    security=[{'Bearer': []}],
    manual_parameters=[
        openapi.Parameter(
            'trip_id',
            openapi.IN_PATH,
            description='ID único da viagem',
            type=openapi.TYPE_STRING,
            format='ObjectId',
            required=True
        )
    ]
)

# Delete Trip
delete_trip_swagger = swagger_auto_schema(
    method='delete',
    operation_id='delete_trip',
    operation_summary='Remove uma viagem',
    operation_description='Remove logicamente uma viagem do sistema (soft delete). A viagem não é removida fisicamente do banco de dados, apenas marcada como excluída.',
    responses={
        200: openapi.Response(
            description='Viagem removida com sucesso',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description='Mensagem de confirmação')
                }
            )
        ),
        400: openapi.Response(description='ID inválido', schema=error_response_schema),
        401: openapi.Response(description='Não autenticado', schema=error_response_schema),
        403: openapi.Response(description='Não autorizado', schema=error_response_schema),
        404: openapi.Response(description='Viagem não encontrada', schema=error_response_schema),
        500: openapi.Response(description='Erro ao processar a requisição', schema=error_response_schema)
    },
    tags=['Trips'],
    security=[{'Bearer': []}],
    manual_parameters=[
        openapi.Parameter(
            'trip_id',
            openapi.IN_PATH,
            description='ID único da viagem a ser removida',
            type=openapi.TYPE_STRING,
            format='ObjectId',
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
