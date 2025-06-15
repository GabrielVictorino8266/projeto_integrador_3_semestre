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
    operation_summary='Login user',
    operation_description='Authenticate user and obtain access/refresh tokens',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['cpf', 'password'],
        properties={
            'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='User CPF number'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password')
        }
    ),
    responses={
        200: openapi.Response(
            description='Authentication successful',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access_token': openapi.Schema(type=openapi.TYPE_STRING, description='JWT access token'),
                    'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='JWT refresh token'),
                    'user': user_schema
                }
            )
        ),
        400: openapi.Response(description='Bad request', schema=validation_error_schema),
        401: openapi.Response(description='Invalid credentials', schema=error_response_schema),
    },
    tags=['Authentication']
)

refresh_swagger = swagger_auto_schema(
    method="post",
    operation_id='refresh',
    operation_summary='Refresh access token',
    operation_description='Obtain a new access token using refresh token',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['refresh_token'],
        properties={
            'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='JWT refresh token')
        }
    ),
    responses={
        200: openapi.Response(
            description='Token refreshed successfully',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access_token': openapi.Schema(type=openapi.TYPE_STRING, description='New JWT access token'),
                    'user': user_schema
                }
            )
        ),
        400: openapi.Response(description='Bad request', schema=validation_error_schema),
        401: openapi.Response(description='Invalid refresh token', schema=error_response_schema),
    },
    tags=['Authentication']
)

logout_swagger = swagger_auto_schema(
    method="post",
    operation_id='logout',
    operation_summary='Logout user',
    operation_description='Invalidate all user tokens',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['refresh_token'],
        properties={
            'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='JWT refresh token')
        }
    ),
    responses={
        200: openapi.Response(description='Logout successful', schema=error_response_schema),
        400: openapi.Response(description='Bad request', schema=validation_error_schema),
        401: openapi.Response(description='Invalid refresh token', schema=error_response_schema),
    },
    tags=['Authentication'],
    security=[{'Bearer': []}]
)

profile_swagger = swagger_auto_schema(
    method="get",
    operation_id='get_profile',
    operation_summary='Get user profile',
    operation_description='Retrieve current user profile information',
    responses={
        200: openapi.Response(
            description='Profile retrieved successfully',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'user': user_schema,
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message')
                }
            )
        ),
        401: openapi.Response(description='Unauthorized', schema=error_response_schema),
        404: openapi.Response(description='User not found', schema=error_response_schema),
    },
    tags=['Profile'],
    security=[{'Bearer': []}]
)
