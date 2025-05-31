# users/swagger/swagger_schemas.py - Versão Simples
from drf_yasg import openapi

# ===== REQUEST SCHEMAS =====
login_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['cpf', 'password'],
    properties={
        'cpf': openapi.Schema(type=openapi.TYPE_STRING, example='18092754314'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, example='minhasenha123'),
    },
)

refresh_token_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['refresh_token'],
    properties={
        'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'),
    },
)

logout_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'),
    },
)

# ===== RESPONSE SCHEMAS =====
login_success_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'access_token': openapi.Schema(type=openapi.TYPE_STRING),
        'refresh_token': openapi.Schema(type=openapi.TYPE_STRING),
        'token_type': openapi.Schema(type=openapi.TYPE_STRING, example='bearer'),
        'expires_in': openapi.Schema(type=openapi.TYPE_INTEGER, example=3600),
        'user': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_STRING),
                'cpf': openapi.Schema(type=openapi.TYPE_STRING),
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'type': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
    }
)

token_refresh_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'access_token': openapi.Schema(type=openapi.TYPE_STRING),
        'token_type': openapi.Schema(type=openapi.TYPE_STRING, example='bearer'),
        'expires_in': openapi.Schema(type=openapi.TYPE_INTEGER, example=3600),
    }
)

user_profile_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id': openapi.Schema(type=openapi.TYPE_STRING),
                'name': openapi.Schema(type=openapi.TYPE_STRING),
                'cpf': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'type': openapi.Schema(type=openapi.TYPE_STRING),
                'telefone': openapi.Schema(type=openapi.TYPE_STRING),
                'active': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        'message': openapi.Schema(type=openapi.TYPE_STRING, example='Perfil obtido com sucesso.'),
    }
)

logout_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, example='Logout realizado com sucesso.'),
    }
)

# ===== ERROR SCHEMA =====
error_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'detail': openapi.Schema(type=openapi.TYPE_STRING)
    }
)

# ===== STANDARD RESPONSES (Para reutilizar em outros endpoints) =====
standard_responses = {
    400: openapi.Response(description="Dados inválidos", schema=error_response_schema),
    401: openapi.Response(description="Não autorizado", schema=error_response_schema),
    403: openapi.Response(description="Acesso negado", schema=error_response_schema),
    500: openapi.Response(description="Erro interno", schema=error_response_schema),
}
