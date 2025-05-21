# users/swagger_decorators.py
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .swagger_schemas import (
    login_request_schema, 
    login_success_response_schema,
    refresh_token_request_schema,
    token_refresh_response_schema,
    user_profile_response_schema,
    standard_responses
)

# Decorator endpoint login
login_swagger = swagger_auto_schema(
    method='post',
    operation_description="Endpoint para autenticação de usuários e obtenção de tokens JWT",
    operation_summary="Login de usuário",
    request_body=login_request_schema,
    responses={
        200: openapi.Response(
            description="Login realizado com sucesso",
            schema=login_success_response_schema
        ),
        **standard_responses
    },
    tags=['Autenticação']
)

# Decorator refresh_token
refresh_token_swagger = swagger_auto_schema(
    method='post',
    operation_description="Endpoint para renovar o token de acesso usando o refresh token",
    operation_summary="Renovar token de acesso",
    request_body=refresh_token_request_schema,
    responses={
        200: openapi.Response(
            description="Token renovado com sucesso",
            schema=token_refresh_response_schema
        ),
        **standard_responses
    },
    tags=['Autenticação']
)

# Decorator user profile
user_profile_swagger = swagger_auto_schema(
    method='get',
    operation_description="Endpoint protegido que retorna o perfil do usuário autenticado",
    operation_summary="Obter perfil do usuário",
    responses={
        200: openapi.Response(
            description="Perfil do usuário obtido com sucesso",
            schema=user_profile_response_schema
        ),
        **standard_responses
    },
    tags=['Usuário'],
    security=[{'Bearer': []}]
)