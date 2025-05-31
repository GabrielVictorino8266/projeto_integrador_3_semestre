# users/controller.py - Versão com Correção do ObjectId
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from datetime import timedelta, datetime
from bson.json_util import dumps
import json
from .swagger.swagger_decorators import *

from .auth_services import (
    auth_user, create_access_token, create_refresh_token, 
    store_refresh_token, validate_refresh_token,
    blacklist_token, invalidate_refresh_token
)
from .authentication import MongoJWTAuthentication

@login_swagger
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Login simples - verifica usuário e senha no banco.
    """
    cpf = request.data.get('cpf')
    password = request.data.get('password')

    if not cpf or not password:
        return Response(
            {"detail": "CPF e senha são obrigatórios."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Aqui é onde verifica usuário e senha no banco
    user = auth_user(cpf, password)
    if not user:
        return Response(
            {"detail": "Usuário ou senha incorretos."},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    # Converter para obter ID
    user_dict = json.loads(dumps(user))
    user_id = user_dict['_id']['$oid']

    # Criar tokens
    access_token = create_access_token(
        data={
            "user_id": user_id,
            "cpf": user.get('cpf'),
            "name": user.get('name'),
            "type": user.get('type')
        },
        expires_delta=timedelta(hours=1)
    )

    refresh_token = create_refresh_token(
        data={
            "user_id": user_id,
            "cpf": user.get('cpf'),
            "name": user.get('name')
        },
        expires_delta=timedelta(days=1)
    )

    # Armazenar refresh token
    store_refresh_token(user_id, refresh_token)

    return Response({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "expires_in": 3600,
        "user": {
            "id": user_id,
            "cpf": user.get('cpf'),
            "name": user.get('name'),
            "email": user.get('email'),
            "type": user.get('type'),
        }
    })

@refresh_token_swagger
@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token_view(request):
    """
    Renovar token de acesso.
    """
    refresh_token = request.data.get('refresh_token')
    if not refresh_token:
        return Response(
            {"detail": "Refresh token é obrigatório."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = validate_refresh_token(refresh_token)
    if not user:
        return Response(
            {"detail": "Refresh token inválido ou expirado."},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    user_dict = json.loads(dumps(user))
    user_id = user_dict['_id']['$oid']

    access_token = create_access_token(
        data={
            "user_id": user_id,
            "cpf": user.get('cpf'),
            "name": user.get('name')
        },
        expires_delta=timedelta(hours=1)
    )

    return Response({
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": 3600
    })

@logout_swagger
@api_view(['POST'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    """
    Logout - invalida tokens.
    """
    try:
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        access_token = auth_header.replace('Bearer ', '') if auth_header.startswith('Bearer ') else None
        refresh_token = request.data.get('refresh_token')
        
        if access_token:
            blacklist_token(access_token)
        
        if refresh_token:
            invalidate_refresh_token(refresh_token)
        
        return Response({
            "message": "Logout realizado com sucesso."
        })
        
    except Exception as e:
        return Response(
            {"detail": f"Erro no logout: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@user_profile_swagger
@api_view(['GET'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """
    Perfil do usuário logado - CORRIGIDO para ObjectId.
    """
    try:
        # request.user agora é SimpleUser
        user = request.user
        
        # CORREÇÃO: Converter os dados do MongoDB corretamente
        user_dict = json.loads(dumps(user.user_data))
        
        return Response({
            "user": {
                "id": user_dict['_id']['$oid'],  # Converter ObjectId corretamente
                "name": user_dict.get('name'),
                "cpf": user_dict.get('cpf'),
                "email": user_dict.get('email'),
                "type": user_dict.get('type'),
                "phone": user_dict.get('phone'),
                "licenseType": user_dict.get('licenseType'),
                "numeroHabilitacao": user_dict.get('numeroHabilitacao'),
                "birthYear": user_dict.get('birthYear'),
                "performance": user_dict.get('performance'),
                "isActive": user_dict.get('isActive')
            },
            "message": "Perfil obtido com sucesso."
        })
        
    except Exception as e:
        print(f"❌ [PROFILE] Erro ao obter perfil: {e}")
        return Response(
            {"detail": f"Erro ao obter perfil: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )