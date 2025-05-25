from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta
from bson.json_util import dumps
import json
from .auth_services import auth_user, create_access_token, create_refresh_token, get_user_from_token
from .authentication import MongoJWTAuthentication
from .swagger.swagger_decorators import login_swagger, refresh_token_swagger, user_profile_swagger

@login_swagger
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
        Login endpoint for user authentication.
    """
    cpf = request.data.get('cpf')
    password = request.data.get('password')
    print(cpf, password)

    if not cpf or not password:
        return Response(
            {
                "detail": "CPF and password are required."
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = auth_user(cpf, password)
    if not user:
        return Response(
            {
                "detail": "Invalid credentials."
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    user_dict = json.loads(dumps(user))

    #create tokens
    access_token_expires = timedelta(hours=1)
    refresh_token_expires = timedelta(days=1)

    access_token = create_access_token(
        data={
            "user_id": user_dict.get('_id'),
            "cpf": user_dict.get('cpf'),
            "type": user_dict.get('type'),
        },
        expires_delta=access_token_expires
    )

    refresh_token = create_refresh_token(
        data={
            "user_id": user_dict.get('_id'),
            "cpf": user_dict.get('cpf'),
            "type": user_dict.get('type'),
        },
        expires_delta=refresh_token_expires
    )


    return Response({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": {
            "id": str(user_dict.get('_id')),
            "cpf": user_dict.get('cpf'),
            "type": user_dict.get('type'),
        }
    })

@refresh_token_swagger
@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    """
    Refresh token endpoint.
    """
    refresh = request.data.get('refresh_token')
    if not refresh:
        return Response(
            {"detail": "Refresh token is required."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = get_user_from_token(refresh)
    if not user:
        return Response(
            {"detail": "Invalid refresh token."},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    user_dict = json.loads(dumps(user))
    access_token_expires = timedelta(hours=1)
    refresh_token_expires = timedelta(days=1)

    access_token = create_access_token(
        data={
            "user_id": user_dict.get('_id'),
            "cpf": user_dict.get('cpf'),
            "type": user_dict.get('type'),
        }    
    )

    return Response({
        "access_token": access_token,
        "token_type": "bearer"
    })

@user_profile_swagger
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([MongoJWTAuthentication])
def get_user_profile(request):
    """
    Get user endpoint and returns user profile which is logged in.
    """
    user = request.user
    user_dict = json.loads(dumps(user))

    return Response({
        "user": {
            "id": str(user_dict.get('_id')),
            "cpf": user_dict.get('cpf'),
            "type": user_dict.get('type'),
            "message": "User profile retrieved successfully."
        }
    })