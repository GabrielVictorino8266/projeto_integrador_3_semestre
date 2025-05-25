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
    operation_description="Endpoint for user authenticattion and token JWT generation",
    operation_summary="User login",
    request_body=login_request_schema,
    responses={
        200: openapi.Response(
            description="User logged successfully",
            schema=login_success_response_schema
        ),
        **standard_responses
    },
    tags=['Authentication']
)

# Decorator refresh_token
refresh_token_swagger = swagger_auto_schema(
    method='post',
    operation_description="Endpoint to renew the access token using the refresh token",
    operation_summary="Renew access token",
    request_body=refresh_token_request_schema,
    responses={
        200: openapi.Response(
            description="New token renewed successfully",
            schema=token_refresh_response_schema
        ),
        **standard_responses
    },
    tags=['Authentication']
)

# Decorator user profile
user_profile_swagger = swagger_auto_schema(
    method='get',
    operation_description="Secured endpoint which returns user profile authenticated data",
    operation_summary="Get user profile",
    responses={
        200: openapi.Response(
            description="User profile retrieved successfully",
            schema=user_profile_response_schema
        ),
        **standard_responses
    },
    tags=['User'],
    security=[{'Bearer': []}]
)