# users/swagger/swagger_decorators.py - Versão Simples
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .swagger_schemas import *

# ===== DECORATORS PARA ENDPOINTS DE USUÁRIO =====

login_swagger = swagger_auto_schema(
    method='post',
    operation_summary="Login",
    operation_description="Autenticação com CPF e senha",
    request_body=login_request_schema,
    responses={
        200: openapi.Response("Login realizado", schema=login_success_response_schema),
        **standard_responses
    },
    tags=['Auth']
)

refresh_token_swagger = swagger_auto_schema(
    method='post',
    operation_summary="Renovar Token",
    operation_description="Gera novo access token usando refresh token",
    request_body=refresh_token_request_schema,
    responses={
        200: openapi.Response("Token renovado", schema=token_refresh_response_schema),
        **standard_responses
    },
    tags=['Auth']
)

user_profile_swagger = swagger_auto_schema(
    method='get',
    operation_summary="Perfil do Usuário",
    operation_description="Retorna dados do usuário logado",
    responses={
        200: openapi.Response("Perfil obtido", schema=user_profile_response_schema),
        **standard_responses
    },
    tags=['User'],
    security=[{'Bearer': []}]
)

logout_swagger = swagger_auto_schema(
    method='post',
    operation_summary="Logout",
    operation_description="Invalida tokens do usuário",
    request_body=logout_request_schema,
    responses={
        200: openapi.Response("Logout realizado", schema=logout_response_schema),
        **standard_responses
    },
    tags=['Auth'],
    security=[{'Bearer': []}]
)

# ===== DECORATORS GENÉRICOS (Para outros endpoints futuros) =====

def create_swagger_decorator(
    method='get',
    summary='',
    description='',
    request_body=None,
    responses=None,
    tag='API',
    requires_auth=False
):
    """
    Factory para criar decorators Swagger facilmente.
    
    Exemplo de uso em outros apps:
    
    product_list_swagger = create_swagger_decorator(
        method='get',
        summary='Listar Produtos',
        description='Retorna lista de produtos',
        tag='Products',
        requires_auth=True
    )
    """
    security = [{'Bearer': []}] if requires_auth else []
    
    if responses is None:
        responses = {200: "Sucesso", **standard_responses}
    
    return swagger_auto_schema(
        method=method,
        operation_summary=summary,
        operation_description=description,
        request_body=request_body,
        responses=responses,
        tags=[tag],
        security=security
    )