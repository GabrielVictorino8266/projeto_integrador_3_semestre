# users/authentication.py - Versão Simples
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from .auth_services import get_user_from_token, is_token_blacklisted
import logging

logger = logging.getLogger(__name__)

class SimpleUser:
    """Classe simples que apenas satisfaz o DRF"""
    def __init__(self, user_data):
        self.user_data = user_data
        self.is_authenticated = True
        self.is_anonymous = False
        self.is_active = True
    
    def __getattr__(self, name):
        # Permite acesso direto aos campos do MongoDB
        return self.user_data.get(name)
    
    def get(self, key, default=None):
        return self.user_data.get(key, default)

class MongoJWTAuthentication(BaseAuthentication):
    """
    Autenticação JWT simples - apenas verifica token válido.
    """
    keyword = 'Bearer'
   
    def authenticate(self, request):
        """Autentica o usuário usando o token JWT"""
        try:
            auth_header = request.META.get('HTTP_AUTHORIZATION')
            
            if not auth_header:
                logger.debug("No authorization header found")
                return None
            
            parts = auth_header.split()
            
            if len(parts) != 2 or parts[0].lower() != self.keyword.lower():
                logger.debug("Invalid authorization header format")
                return None
            
            token = parts[1]
            return self.authenticate_credentials(token)
            
        except Exception as e:
            logger.error(f"Error during authentication: {str(e)}")
            raise AuthenticationFailed(_('Erro durante a autenticação'))
    
    def authenticate_credentials(self, token):
        """
        Valida token e retorna usuário.
        """
        try:
            # Verificar se token está na blacklist
            if is_token_blacklisted(token):
                logger.warning(f"Token {token[:10]}... revoked")
                raise AuthenticationFailed(_('Token foi revogado'))
            
            # Obter usuário do token
            user_data = get_user_from_token(token)

            if user_data is None:
                logger.warning(f"Invalid token: {token[:10]}...")
                raise AuthenticationFailed(_('Token inválido'))
            
            # Criar usuário simples
            user = SimpleUser(user_data)
            logger.info(f"User {user.name} authenticated successfully")
            
            return (user, token)
            
        except AuthenticationFailed:
            raise
        except Exception as e:
            logger.error(f"Error validating token: {str(e)}")
            raise AuthenticationFailed(_('Erro ao validar token'))
    
    def authenticate_header(self, request):
        return self.keyword