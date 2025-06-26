from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import serializers

# Error response schemas
error_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'detail': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
    }
)

validation_error_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'field_name': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING),
            description='Field validation errors'
        ),
        'non_field_errors': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(type=openapi.TYPE_STRING),
            description='General validation errors'
        ),
    }
)

# Define user schema
user_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_STRING, description='User ID'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='User name'),
        'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='User CPF number'),
        'type': openapi.Schema(type=openapi.TYPE_STRING, description='User type'),
        'phone': openapi.Schema(type=openapi.TYPE_STRING, description='User phone number'),
        'licenseType': openapi.Schema(type=openapi.TYPE_STRING, description='License type'),
        'licenseNumber': openapi.Schema(type=openapi.TYPE_STRING, description='License number'),
        'birthYear': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Birth year'
        ),
        'performance': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description='User performance metrics'
        ),
        'isActive': openapi.Schema(
            type=openapi.TYPE_BOOLEAN,
            description='User active status'
        )
    },
    required=['id', 'name', 'cpf']
)

# Swagger decorators
login_swagger = swagger_auto_schema(
    method="post",
    operation_id='login',
    operation_summary='Autenticação de usuário',
    operation_description='Autentica o usuário e retorna os tokens de acesso e refresh',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['cpf', 'password'],
        properties={
            'cpf': openapi.Schema(
                type=openapi.TYPE_STRING, 
                description='CPF do usuário (apenas números)',
                example='12345678900'
            ),
            'password': openapi.Schema(
                type=openapi.TYPE_STRING, 
                description='Senha do usuário',
                format='password'
            )
        }
    ),
    responses={
        200: openapi.Response(
            description='Autenticação realizada com sucesso',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access_token': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description='Token JWT de acesso (válido por 2 horas)'
                    ),
                    'refresh_token': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description='Token JWT de refresh (válido por 24 horas)'
                    ),
                    'user': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_STRING, description='ID único do usuário'),
                            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do usuário'),
                            'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='CPF do usuário'),
                            'type': openapi.Schema(type=openapi.TYPE_STRING, description='Tipo de usuário')
                        }
                    )
                }
            )
        ),
        400: openapi.Response(
            description='Requisição inválida', 
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='CPF e Senha são necessários para a requisição'
                    )
                }
            )
        ),
        401: openapi.Response(
            description='Credenciais inválidas', 
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='CPF ou Senha não são válidos, verifique os e tente novamente.'
                    )
                }
            )
        ),
        500: openapi.Response(
            description='Erro interno do servidor',
            schema=error_response_schema
        )
    },
    tags=['Autenticação']
)

refresh_swagger = swagger_auto_schema(
    method="post",
    operation_id='refresh_token',
    operation_summary='Atualizar token de acesso',
    operation_description='Obtém um novo token de acesso usando o token de refresh',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['refresh_token'],
        properties={
            'refresh_token': openapi.Schema(
                type=openapi.TYPE_STRING, 
                description='Token de refresh JWT',
                example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
            )
        }
    ),
    responses={
        200: openapi.Response(
            description='Token atualizado com sucesso',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access_token': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        description='Novo token JWT de acesso (válido por 1 hora)'
                    ),
                    'user': openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_STRING, description='ID único do usuário'),
                            'name': openapi.Schema(type=openapi.TYPE_STRING, description='Nome do usuário'),
                            'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='CPF do usuário')
                        }
                    )
                }
            )
        ),
        400: openapi.Response(
            description='Requisição inválida', 
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='Refresh Token é necessário, verifique-o e envie novamente.'
                    )
                }
            )
        ),
        401: openapi.Response(
            description='Token de refresh inválido', 
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='Refresh Token é inválido ou está expirado, verifique-o e tente novamente.'
                    )
                }
            )
        )
    },
    tags=['Autenticação']
)

logout_swagger = swagger_auto_schema(
    method="post",
    operation_id='logout',
    operation_summary='Efetuar logout',
    operation_description='Invalida todos os tokens do usuário, forçando um novo login',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['refresh_token'],
        properties={
            'refresh_token': openapi.Schema(
                type=openapi.TYPE_STRING, 
                description='Token de refresh JWT que será invalidado',
                example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
            )
        }
    ),
    responses={
        200: openapi.Response(
            description='Logout realizado com sucesso', 
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='Logout realizado com sucesso.'
                    )
                }
            )
        ),
        400: openapi.Response(
            description='Requisição inválida', 
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='Refresh Token é necessário, verifique-o e envie novamente.'
                    )
                }
            )
        ),
        401: openapi.Response(
            description='Não autorizado', 
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='Refresh Token não é válido, verifique-o'
                    )
                }
            )
        ),
        500: openapi.Response(
            description='Erro interno do servidor',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='Error processing logout.'
                    )
                }
            )
        )
    },
    tags=['Autenticação'],
    security=[{'Bearer': []}]
)

profile_swagger = swagger_auto_schema(
    method="get",
    operation_id='obter_perfil',
    operation_summary='Obter perfil do usuário',
    operation_description='Retorna as informações do perfil do usuário autenticado',
    responses={
        200: openapi.Response(
            description='Perfil obtido com sucesso',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_STRING, description='ID único do usuário'),
                    'name': openapi.Schema(type=openapi.TYPE_STRING, description='Nome completo do usuário'),
                    'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='CPF do usuário (apenas números)'),
                    'type': openapi.Schema(type=openapi.TYPE_STRING, description='Tipo de usuário'),
                    'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Número de telefone', nullable=True),
                    'licenseType': openapi.Schema(type=openapi.TYPE_STRING, description='Tipo de CNH', nullable=True),
                    'licenseNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Número da CNH', nullable=True),
                    'birthYear': openapi.Schema(type=openapi.TYPE_INTEGER, description='Ano de nascimento', nullable=True),
                    'performance': openapi.Schema(type=openapi.TYPE_OBJECT, description='Métricas de desempenho', nullable=True),
                    'isActive': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Status de ativação do usuário')
                }
            )
        ),
        401: openapi.Response(
            description='Não autenticado', 
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='As credenciais de autenticação não foram fornecidas.'
                    )
                }
            )
        ),
        404: openapi.Response(
            description='Usuário não encontrado', 
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'detail': openapi.Schema(
                        type=openapi.TYPE_STRING, 
                        example='Usuário não encontrado ao tentar recuperar o perfil.'
                    )
                }
            )
        )
    },
    tags=['Perfil'],
    security=[{'Bearer': []}]
)
