# users/views.py
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.conf import settings
from users.auth_services import auth_user, create_token, store_refresh_token, get_user_from_token, invalidate_user_tokens
from users.auth_services import is_token_blacklisted, blacklist_token
from users.auth_services import cleanup_expired_tokens
from mongoengine import connection
import logging
from users.authentication import MongoJWTAuthentication

logger = logging.getLogger(__name__)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Login - check user and password in database.
    Return access and refresh tokens.
    """
    cpf = request.data.get('cpf')
    password = request.data.get('password')

    if not cpf or not password:
        return Response(
            {"detail": "CPF and password are required."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = auth_user(cpf, password)
    if not user:
        return Response(
            {"detail": "CPF or password are invalid."},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # Create tokens
    access_token = create_token(
        {
            "user_id": str(user["_id"]),
            "name": user.get("name"),
            "cpf": user.get("cpf")
        },
        token_type="access",
        expires_hours=2
    )
    
    refresh_token = create_token(
        {"user_id": str(user["_id"])},
        token_type="refresh",
        expires_hours=24
    )

    # Store refresh token
    if not store_refresh_token(str(user["_id"]), refresh_token):
        return Response(
            {"detail": "Error storing refresh token."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return Response(
        {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": {
                "id": str(user["_id"]),
                "name": user.get("name"),
                "cpf": user.get("cpf"),
                "type": user.get("type")
            }
        },
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh(request):
    """
    Refresh access token using refresh token.
    """
    refresh_token = request.data.get('refresh_token')
    
    if not refresh_token:
        return Response(
            {"detail": "Refresh token is required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Get user from refresh token
    user = get_user_from_token(refresh_token)
    if not user:
        return Response(
            {"detail": "Refresh token is invalid or expired."},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # Create new access token
    access_token = create_token(
        {
            "user_id": str(user["_id"]),
            "name": user.get("name"),
            "cpf": user.get("cpf")
        },
        token_type="access",
        expires_hours=1
    )

    return Response(
        {
            "access_token": access_token,
            "user": {
                "id": str(user["_id"]),
                "name": user.get("name"),
                "cpf": user.get("cpf")
            }
        },
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([MongoJWTAuthentication])
def logout(request):
    """
    Logout - invalidates all user's tokens.
    """
    refresh_token = request.data.get('refresh_token')
    
    if not refresh_token:
        return Response(
            {"detail": "Refresh token is required."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        # Get user ID from request
        user_id = request.user.get("_id")
        
        # Check if refresh token exists in database
        db = connection.get_db()
        refresh_token_doc = db['refresh_tokens'].find_one({"token": refresh_token})
        if not refresh_token_doc:
            return Response(
                {"detail": "Invalid refresh token."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Invalidate all user's tokens
        if invalidate_user_tokens(user_id):
            return Response(
                {"detail": "Logout successful."},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"detail": "Error invalidating tokens."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    except Exception as e:
        logger.error(f"Error processing logout: {str(e)}")
        return Response(
            {"detail": "Error processing logout."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([MongoJWTAuthentication])
def user_profile(request):
    """
    Get current user's profile information.
    """
    try:
        # Get user ID from request
        user_id = request.user.get("_id")
        
        # Get user data from auth_services
        user = get_user_from_token(request.auth)
        if not user:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )
            
        profile_data = {
            "id": str(user["_id"]),
            "name": user.get("name"),
            "cpf": user.get("cpf"),
            "type": user.get("type"),
            "phone": user.get("phone"),
            "licenseType": user.get("licenseType"),
            "licenseNumber": user.get("licenseNumber"),
            "birthYear": user.get("birthYear"),
            "performance": user.get("performance"),
            "isActive": user.get("isActive")
        }
        
        return Response(
            {"user": profile_data, "message": "Profile obtained successfully."},
            status=status.HTTP_200_OK
        )
        
    except Exception as e:
        logger.error(f"Error getting profile: {str(e)}")
        return Response(
            {"detail": "Error getting profile."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )