"""
    Simple exceptions for the drivers API.
"""

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

class DriverNotFoundException(Exception):
    """
    Driver not found.
    """
    pass

class DriverCPFInvalidException(Exception):
    """
    Driver cpf is not valid.
    """
    pass


# =====================================
# HANDLER GLOBAL
# =====================================

def custom_exception_handler(exc, context):
    """
    Custom exception handler for the drivers API.
    """
    response = exception_handler(exc, context)
    # 1. Check if there is already a response for the exception.
    # If there is, just return it.
    if response is not None:
        return response

    if isinstance(exc, DriverNotFoundException):
        return Response(
            {'error': 'Driver not found.'},
            status=status.HTTP_404_NOT_FOUND
        )

    elif isinstance(exc, DriverCPFInvalidException):
        return Response(
            {'error': 'Driver CPF is not valid.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    else:
        return Response(
            {'error': 'An unexpected error occurred.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
