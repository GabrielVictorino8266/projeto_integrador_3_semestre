from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .test_setup import UsersTestCase
from freezegun import freeze_time

class RefreshTokenTest(UsersTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('users:refresh_token')
        
    def test_refresh_success(self):
        """
        Testa o refresh token com sucesso usando refresh token válido.
        """
        # Primeiro faz login para obter refresh token
        with freeze_time("2025-06-15 08:00:00"):
            login_response = self.client.post(reverse('users:login'), {
                'cpf': self.valid_user_data['cpf'],
                'password': self.valid_user_data['password']
            }, format='json')
            self.assertEqual(login_response.status_code, status.HTTP_200_OK)
            
            refresh_token = login_response.data['refresh_token']
            
            # Agora tenta refresh
            response = self.client.post(self.url, {
                'refresh_token': refresh_token
            }, format='json')
            
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIn('access_token', response.data)
            self.assertIn('user', response.data)
            
            # Verifica que o novo access token expira em 2 horas
            with freeze_time("2025-06-15 10:01:00"):
                # Testa token de acesso expirado
                profile_url = reverse('users:user_profile')
                self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access_token"]}')
                profile_response = self.client.get(profile_url)
                self.assertEqual(profile_response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_refresh_missing_token(self):
        """
        Testa tentativa de refresh sem token.
        """
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Refresh token is required.')
        
    def test_refresh_invalid_token(self):
        """
        Testa tentativa de refresh com token inválido.
        """
        response = self.client.post(self.url, {
            'refresh_token': 'invalid_token'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Refresh token is invalid or expired.')
    
    def test_refresh_expired_token(self):
        """
        Testa tentativa de refresh com token expirado.
        """
        # Primeiro faz login para obter refresh token
        with freeze_time("2025-06-15 08:00:00"):
            login_response = self.client.post(reverse('users:login'), {
                'cpf': self.valid_user_data['cpf'],
                'password': self.valid_user_data['password']
            }, format='json')
            self.assertEqual(login_response.status_code, status.HTTP_200_OK)
            
            refresh_token = login_response.data['refresh_token']
        
        # Avança o tempo para depois da expiração do refresh token (24h + 1min)
        with freeze_time("2025-06-16 08:01:00"):
            # Agora tenta refresh
            response = self.client.post(self.url, {
                'refresh_token': refresh_token
            }, format='json')
            
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertEqual(response.data['detail'], 'Refresh token is invalid or expired.')
