from drf_yasg import openapi

# Request Schemas
login_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['cpf', 'password'],
    properties={
        'cpf': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='User CPF (numbers only)',
            example='12345678901'
        ),
        'password': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='User password',
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
            description='Refresh Token JWT',
            example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        ),
    },
)

# Response Schemas
user_data_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    description='Basic user data',
    properties={
        'id': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='User ID in MongoDB',
            example='682a1fc56a7154a8bfbe0529'
        ),
        'cpf': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='User CPF (numbers only)',
            example='12345678901'
        ),
        'tipo': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='User Type',
            example='admin'
        ),
    }
)

login_success_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'access_token': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Success Token JWT',
            example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        ),
        'refresh_token': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Refresh Token JWT',
            example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        ),
        'token_type': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Token Type',
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
            description='New token JWT for access',
            example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
        ),
        'token_type': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='Token Type',
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
                    description='User ID in MongoDB',
                    example='682a1fc56a7154a8bfbe0529'
                ),
                'cpf': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='User CPF (numbers only)',
                    example='12345678901'
                ),
                'tipo': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='User type',
                    example='admin'
                ),
                'message': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Success message',
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
            description='Error message'
        )
    }
)

# Common Responses
standard_responses = {
    400: openapi.Response(
        description="Invalid input data",
        schema=error_response_schema,
        examples={
            'application/json': {
                'detail': 'User cpf and password are required'
            }
        }
    ),
    401: openapi.Response(
        description="Invalid Credentials",
        schema=error_response_schema,
        examples={
            'application/json': {
                'detail': 'Invalid credentials.'
            }
        }
    ),
    403: openapi.Response(
        description="Access Denied",
        schema=error_response_schema,
        examples={
            'application/json': {
                'detail': 'Authentication credentials were not provided.'
            }
        }
    ),
}