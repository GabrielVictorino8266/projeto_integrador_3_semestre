from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils.translation import gettext_lazy as _
from .auth_services import get_user_from_token

class MongoJWTAuthentication(BaseAuthentication):
    """
        Custom authentication class for JWT authentication with MongoDB.
    """
    keyword = 'Bearer'
   
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None
        
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != self.keyword.lower():
            return None
    
        token = parts[1]
        return self.authenticate_credentials(token)
    
    def authenticate_credentials(self, token):
        """
            Validate token and get user
        """
        user = get_user_from_token(token)

        if user is None:
            raise AuthenticationFailed(_('Invalid token'))
        
        if not user.get('active', True):
            raise AuthenticationFailed(_('User is inactive'))
        
        return (user, token)
    
    def authenticate_header(self, request):
        """
            Value for the headers WWW-Authenticate when authentication fails
        """
        
        return self.keyword
