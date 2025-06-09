from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from drivers.serializers import DriverSerializer
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

# Define the driver schema using openapi.Schema
driver_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_STRING, description='Driver ID'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Driver password'),
        'cpf': openapi.Schema(type=openapi.TYPE_STRING, description='Driver CPF number'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Driver email'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Driver name'),
        'birthYear': openapi.Schema(
            type=openapi.TYPE_STRING,
            format='date',
            description='Driver birth year'
        ),
        'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Driver phone number'),
        'licenseType': openapi.Schema(type=openapi.TYPE_STRING, description='Type of driver license'),
        'licenseNumber': openapi.Schema(type=openapi.TYPE_STRING, description='Driver license number'),
        'performance': openapi.Schema(
            type=openapi.TYPE_INTEGER,
            description='Driver performance score'
        ),
        'incidents': openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_STRING, description='Incident ID'),
                    'type': openapi.Schema(type=openapi.TYPE_STRING, description='Incident type'),
                    'date': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        format='date-time',
                        description='Incident date'
                    ),
                    'description': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description='Incident description'
                    )
                }
            ),
            description='List of driver incidents'
        ),
        'isActive': openapi.Schema(
            type=openapi.TYPE_BOOLEAN,
            description='Driver active status'
        ),
        'type': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='User type'
        ),
        'createdAt': openapi.Schema(
            type=openapi.TYPE_STRING,
            format='date-time',
            description='Driver creation date'
        ),
        'updatedAt': openapi.Schema(
            type=openapi.TYPE_STRING,
            format='date-time',
            description='Driver last update date'
        )
    },
    required=['password', 'cpf', 'email', 'name', 'birthYear', 'phone', 'licenseType', 'licenseNumber', 'type']
)

# Swagger decorators
list_drivers_swagger = swagger_auto_schema(
    method="get",
    operation_id='list_drivers',
    operation_summary='List all drivers',
    operation_description='List all drivers with pagination',
    manual_parameters=[
        openapi.Parameter(
            'page',
            openapi.IN_QUERY,
            description='Page number (optional)',
            type=openapi.TYPE_INTEGER,
            required=False,
        ),
        openapi.Parameter(
            'limit',
            openapi.IN_QUERY,
            description='Number of items per page (optional)',
            type=openapi.TYPE_INTEGER,
            required=False,
        ),
        openapi.Parameter(
            'isActive',
            openapi.IN_QUERY,
            description='Filter by active status (optional)',
            type=openapi.TYPE_BOOLEAN,
            required=False,
        ),
        openapi.Parameter(
            'licenseType',
            openapi.IN_QUERY,
            description='Filter by license type (optional)',
            type=openapi.TYPE_STRING,
            required=False,
        ),
    ],
    responses={
        200: openapi.Response(
            description='List of drivers',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'count': openapi.Schema(type=openapi.TYPE_INTEGER, description='Total number of drivers'),
                    'next': openapi.Schema(type=openapi.TYPE_STRING, description='URL for next page'),
                    'previous': openapi.Schema(type=openapi.TYPE_STRING, description='URL for previous page'),
                    'results': openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=driver_schema,
                        description='List of driver objects'
                    )
                }
            )
        ),
        400: openapi.Response(description='Invalid request', schema=validation_error_schema),
        401: openapi.Response(description='Unauthorized', schema=error_response_schema),
    },
    tags=['Drivers'],
    security=[{'Bearer': []}]
)

create_driver_swagger = swagger_auto_schema(
    method="post",
    operation_id='create_driver',
    operation_summary='Create driver',
    operation_description='Create a new driver with the provided data',
    request_body=driver_schema,
    responses={
        201: openapi.Response(description='Driver created successfully'),
        400: openapi.Response(description='Invalid request', schema=validation_error_schema),
        401: openapi.Response(description='Unauthorized', schema=error_response_schema),
    },
    tags=['Drivers'],
    security=[{'Bearer': []}]
)

get_driver_swagger = swagger_auto_schema(
    method="get",
    operation_id='get_driver',
    operation_summary='Get driver details',
    operation_description='Get details of a specific driver by ID',
    manual_parameters=[
        openapi.Parameter(
            'driver_id',
            openapi.IN_PATH,
            description='Driver ID',
            type=openapi.TYPE_STRING,
            required=True,
        )
    ],
    responses={
        200: openapi.Response(description='Driver details', schema=driver_schema),
        404: openapi.Response(description='Driver not found', schema=error_response_schema),
        401: openapi.Response(description='Unauthorized', schema=error_response_schema),
    },
    tags=['Drivers'],
    security=[{'Bearer': []}]
)

update_driver_swagger = swagger_auto_schema(
    method="put",
    operation_id='update_driver',
    operation_summary='Update driver',
    operation_description='Update driver information',
    request_body=driver_schema,
    manual_parameters=[
        openapi.Parameter(
            'driver_id',
            openapi.IN_PATH,
            description='Driver ID',
            type=openapi.TYPE_STRING,
            required=True,
        )
    ],
    responses={
        200: openapi.Response(description='Driver updated successfully', schema=driver_schema),
        400: openapi.Response(description='Invalid request', schema=validation_error_schema),
        404: openapi.Response(description='Driver not found', schema=error_response_schema),
        401: openapi.Response(description='Unauthorized', schema=error_response_schema),
    },
    tags=['Drivers'],
    security=[{'Bearer': []}]
)

delete_driver_swagger = swagger_auto_schema(
    method="delete",
    operation_id='delete_driver',
    operation_summary='Delete driver',
    operation_description='Delete a driver by ID',
    manual_parameters=[
        openapi.Parameter(
            'driver_id',
            openapi.IN_PATH,
            description='Driver ID',
            type=openapi.TYPE_STRING,
            required=True,
        )
    ],
    responses={
        204: openapi.Response(description='Driver deleted successfully'),
        404: openapi.Response(description='Driver not found', schema=error_response_schema),
        401: openapi.Response(description='Unauthorized', schema=error_response_schema),
    },
    tags=['Drivers'],
    security=[{'Bearer': []}]
)
