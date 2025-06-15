from rest_framework import status
from .test_setup import UsersTestCase
from freezegun import freeze_time
import time

class TestTokenExpiration(UsersTestCase):
    @freeze_time("2025-06-15 08:30:00")  # Define um ponto de partida fixo
    def test_access_token_expiration(self):
        """
        Testa se o token de acesso expira após 2 horas
        """
        # Faz login para obter tokens
        login_response = self.client.post(self.get_login_url(), {
            'cpf': self.valid_user_data['cpf'],
            'password': self.valid_user_data['password']
        }, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        
        access_token = login_response.data['access_token']
        
        # Avança o tempo em 2 hora e 1 minuto
        with freeze_time("2025-06-15 10:31:00"):
            # Tenta usar o token expirado
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
            response = self.client.get(self.get_profile_url())
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            
    @freeze_time("2025-06-15 08:30:00")
    def test_refresh_token_expiration(self):
        """
        Testa se o token de refresh expira após 1 dia
        """
        # Faz login para obter tokens
        login_response = self.client.post(self.get_login_url(), {
            'cpf': self.valid_user_data['cpf'],
            'password': self.valid_user_data['password']
        }, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        
        refresh_token = login_response.data['refresh_token']
        
        # Avança o tempo em 1 dia e 1 minuto
        with freeze_time("2025-06-16 11:31:00"):
            # Tenta refresh com token expirado
            response = self.client.post('/api/users/refresh-token/', {
                'refresh_token': refresh_token
            }, format='json')
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            
    @freeze_time("2025-06-15 09:00:00")
    def test_token_blacklisting(self):
        """
        Testa se o token é corretamente invalidado no logout
        """
        # Faz login para obter tokens
        login_response = self.client.post(self.get_login_url(), {
            'cpf': self.valid_user_data['cpf'],
            'password': self.valid_user_data['password']
        }, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        
        access_token = login_response.data['access_token']
        refresh_token = login_response.data['refresh_token']
        
        # Faz logout para invalidar tokens
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        logout_response = self.client.post(self.get_logout_url(), {
            'refresh_token': refresh_token
        }, format='json')
        self.assertEqual(logout_response.status_code, status.HTTP_200_OK)
        
        # Avança o tempo em 1 hora para garantir que o token de acesso expirou
        with freeze_time("2025-06-15 11:10:00"):
            # Testa token de acesso
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
            profile_response = self.client.get(self.get_profile_url())
            self.assertEqual(profile_response.status_code, status.HTTP_401_UNAUTHORIZED)
            
        # Testa token de refresh
        refresh_response = self.client.post(self.get_refresh_url(), {
            'refresh_token': refresh_token
        }, format='json')
        self.assertEqual(refresh_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def get_login_url(self):
        return '/api/users/login/'

    def get_profile_url(self):
        return '/api/users/profile/'

    def get_refresh_url(self):
        return '/api/users/refresh-token/'

    def get_logout_url(self):
        return '/api/users/logout/'
