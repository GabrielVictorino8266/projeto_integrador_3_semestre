from drf_yasg import openapi

# Request Schemas
login_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['cpf', 'senha'],
    properties={
        'cpf': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='CPF do usuário (somente números)',
            example='12345678901'
        ),
        'senha': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Senha do usuário',
            example='9012004'
        ),
    },
)

refresh_token_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['refresh_token'],
    properties={
        'refresh_token': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Token JWT de refresh',
            example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        ),
    },
)

# Response Schemas
user_data_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    description='Dados básicos do usuário',
    properties={
        'id': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='ID do usuário no MongoDB',
            example='682a1fc56a7154a8bfbe0529'
        ),
        'cpf': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='CPF do usuário',
            example='12345678901'
        ),
        'tipo': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Tipo do usuário',
            example='admin'
        ),
    }
)

login_success_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'access_token': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Token JWT de acesso',
            example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        ),
        'refresh_token': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Token JWT de refresh',
            example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        ),
        'token_type': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Tipo do token',
            example='bearer'
        ),
        'user': user_data_schema,
    }
)

token_refresh_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'access_token': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Novo token JWT de acesso',
            example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        ),
        'token_type': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Tipo do token',
            example='bearer'
        ),
    }
)

user_profile_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='ID do usuário no MongoDB',
                    example='682a1fc56a7154a8bfbe0529'
                ),
                'cpf': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='CPF do usuário',
                    example='12345678901'
                ),
                'tipo': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Tipo do usuário',
                    example='admin'
                ),
                'message': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Mensagem de confirmação',
                    example='User profile retrieved successfully.'
                ),
            }
        ),
    }
)

# Error Schemas
error_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'detail': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Mensagem de erro'
        )
    }
)

# Common Responses
standard_responses = {
    400: openapi.Response(
        description="Dados de entrada inválidos",
        schema=error_response_schema,
        examples={
            'application/json': {
                'detail': 'CPF e senha são obrigatórios'
            }
        }
    ),
    401: openapi.Response(
        description="Credenciais inválidas",
        schema=error_response_schema,
        examples={
            'application/json': {
                'detail': 'Invalid credentials.'
            }
        }
    ),
    403: openapi.Response(
        description="Acesso negado",
        schema=error_response_schema,
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
}