from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from vehicles.serializer import VehicleSerializer
from vehicles.types import VehicleStatus

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

create_vehicle_swagger = swagger_auto_schema(
    method="post",
    operation_id='create_vehicle',
    operation_summary='Criação de veículo',
    operation_description='Cria um veículo com os dados informados',
    request_body=VehicleSerializer(),
    responses={
        201: openapi.Response(description='Veículo criado com sucesso'),
        400: openapi.Response(description='Requisição inválida', schema=validation_error_schema),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
    },
    tags=['Vehicle'],
    security=[{'Bearer': []}]
)

update_vehicle_swagger = swagger_auto_schema(
    method="put",
    operation_id='update_vehicle',
    operation_summary='Atualização de veículo',
    operation_description='Atualiza um veículo com os dados informados',
    request_body=VehicleSerializer(),
    responses={
        200: openapi.Response(description='Veículo atualizado com sucesso'),
        400: openapi.Response(description='Requisição inválida', schema=validation_error_schema),
        404: openapi.Response(description='Veículo não encontrado', schema=error_response_schema),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
    },
    tags=['Vehicle'],
    security=[{'Bearer': []}]
)

delete_vehicle_swagger = swagger_auto_schema(
    method="delete",
    operation_id='delete_vehicle',
    operation_summary='Exclusão de veículo',
    operation_description='Deleta um veículo',
    responses={
        204: openapi.Response(description='Veículo deletado com sucesso'),
        400: openapi.Response(description='Requisição inválida', schema=validation_error_schema),
        404: openapi.Response(description='Veículo não encontrado', schema=error_response_schema),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
    },
    tags=['Vehicle'],
    security=[{'Bearer': []}]
)

list_vehicles_swagger = swagger_auto_schema(
    method="get",
    operation_id='list_vehicles',
    operation_summary='Listagem de veículos',
    operation_description='Lista todos os veículos com paginação',
    manual_parameters=[
        openapi.Parameter(
            'page',
            openapi.IN_QUERY,
            description='Número da página (opcional)',
            type=openapi.TYPE_INTEGER,
            required=False,
        ),
        openapi.Parameter(
            'limit',
            openapi.IN_QUERY,
            description='Número de itens por página (opcional)',
            type=openapi.TYPE_INTEGER,
            required=False,
        ),
        openapi.Parameter(
            'status',
            openapi.IN_QUERY,
            description='Filtro por status do veículo (opcional)',
            enum=VehicleStatus.choices,
            type=openapi.TYPE_STRING,
            required=False,
            explode=True,
        ),
        openapi.Parameter(
            'licensePlate',
            openapi.IN_QUERY,
            description='Filtro por placa do veículo (opcional)',
            type=openapi.TYPE_STRING,
            required=False,
        ),
    ],
    responses={
        200: openapi.Response(
            description='Lista paginada de veículos',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'total': openapi.Schema(type=openapi.TYPE_INTEGER, description='Total de registros'),
                    'per_page': openapi.Schema(type=openapi.TYPE_INTEGER, description='Itens por página'),
                    'current_page': openapi.Schema(type=openapi.TYPE_INTEGER, description='Página atual'),
                    'last_page': openapi.Schema(type=openapi.TYPE_INTEGER, description='Última página'),
                    'first_page_url': openapi.Schema(type=openapi.TYPE_STRING, description='URL da primeira página'),
                    'last_page_url': openapi.Schema(type=openapi.TYPE_STRING, description='URL da última página'),
                    'next_page_url': openapi.Schema(type=openapi.TYPE_STRING, description='URL da próxima página'),
                    'prev_page_url': openapi.Schema(type=openapi.TYPE_STRING, description='URL da página anterior'),
                    'path': openapi.Schema(type=openapi.TYPE_STRING, description='Caminho base da API'),
                    'from': openapi.Schema(type=openapi.TYPE_INTEGER, description='Primeiro item da página atual'),
                    'to': openapi.Schema(type=openapi.TYPE_INTEGER, description='Último item da página atual'),
                    'items': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        description='Lista de veículos',
                        items=openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            description='Dados do veículo'
                        )
                    )
                }
            )
        ),
        400: openapi.Response(description='Requisição inválida', schema=validation_error_schema),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
    },
    tags=['Vehicle'],
    security=[{'Bearer': []}]
)

get_vehicle_swagger = swagger_auto_schema(
    method="get",
    operation_id='get_vehicle',
    operation_summary='Obter veículo',
    operation_description='Obtém um veículo pelo ID',
    manual_parameters=[
        openapi.Parameter(
            'id',
            openapi.IN_PATH,
            description="ID do veículo",
            type=openapi.TYPE_STRING,
            required=True,
        )
    ],
    responses={
        200: openapi.Response(description='Detalhes do veículo', schema=VehicleSerializer()),
        400: openapi.Response(description='Requisição inválida', schema=validation_error_schema),
        404: openapi.Response(description='Veículo não encontrado', schema=error_response_schema),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
    },
    tags=['Vehicle'],
    security=[{'Bearer': []}]
)

list_vehicle_status_swagger = swagger_auto_schema(
    method="get",
    operation_id='list_vehicle_status',
    operation_summary='Listagem de status de veículos',
    operation_description='Lista todos os status de veículos',
    responses={
        200: openapi.Response(description='Lista de status de veículos', schema=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'value': openapi.Schema(type=openapi.TYPE_STRING, description='Valor do status'),
                    'label': openapi.Schema(type=openapi.TYPE_STRING, description='Descrição do status')
                }
            )
        )),
        401: openapi.Response(description='Não autorizado', schema=error_response_schema),
    },
    tags=['Vehicle'],
    security=[{'Bearer': []}]
)
