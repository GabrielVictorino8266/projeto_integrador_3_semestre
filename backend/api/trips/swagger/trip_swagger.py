from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from trips.serializers import TripSerializer
from rest_framework import serializers

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
    security=[{'Bearer': []}]
)