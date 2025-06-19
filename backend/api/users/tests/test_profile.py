from rest_framework import status
from .test_setup import UsersTestCase
from freezegun import freeze_time

class ProfileTest(UsersTestCase):
    def test_get_profile_success(self):
        """
        Testa obtenção de perfil com sucesso usando token válido.
        """
        # Primeiro faz login para obter access token
        with freeze_time("2025-06-15 08:00:00"):
            login_response = self.client.post(self.login_url, {
                'cpf': self.valid_user_data['cpf'],
                'password': self.plain_password
            }, format='json')
            self.assertEqual(login_response.status_code, status.HTTP_200_OK)
            
            access_token = login_response.data['access_token']
            
            # Configura o token no header e obtém o perfil
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
            response = self.client.get(self.profile_url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            
            # Verifica os campos retornados
            expected_fields = ['id', 'name', 'cpf', 'type', 'phone', 'licenseType',
                             'licenseNumber', 'birthYear', 'performance', 'isActive']
            for field in expected_fields:
                self.assertIn(field, response.data['user'])
            
            self.assertEqual(response.data['message'], 'Profile obtained successfully.')
            
            # Verifica que o perfil corresponde ao usuário criado
            self.assertEqual(response.data['user']['cpf'], self.valid_user_data['cpf'])
            self.assertEqual(response.data['user']['name'], self.valid_user_data['name'])
            self.assertEqual(response.data['user']['type'], self.valid_user_data['type'])
    
    def test_get_profile_unauthorized(self):
        """
        Testa tentativa de obter perfil sem token.
        """
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
    
    def test_get_profile_with_invalid_token(self):
        """
        Testa tentativa de obter perfil com token inválido.
        """
        self.client.credentials(HTTP_AUTHORIZATION='Bearer invalid_token')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    @freeze_time("2025-06-15 08:00:00")
    def test_get_profile_after_logout(self):
        """
        Testa tentativa de obter perfil após logout.
        
        Note: In JWT authentication, access tokens are stateless and cannot be
        invalidated. They remain valid until they expire (2 hours). Only refresh
        tokens are stored in the database and can be invalidated during logout.
        """
        # Primeiro faz login para obter tokens
        login_response = self.client.post(self.login_url, {
            'cpf': self.valid_user_data['cpf'],
            'password': self.plain_password
        }, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        
        access_token = login_response.data['access_token']
        refresh_token = login_response.data['refresh_token']
        
        # Configura o token e verifica que funciona antes do logout
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        profile_response = self.client.get(self.profile_url)
        self.assertEqual(profile_response.status_code, status.HTTP_200_OK)
        
        # Faz logout (should invalidate refresh token only)
        logout_response = self.client.post(self.logout_url, {
            'refresh_token': refresh_token
        }, format='json')
        self.assertEqual(logout_response.status_code, status.HTTP_200_OK)
        
        # Tenta obter perfil após logout - should still work because access token is valid
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Aguarda mais do que o tempo de expiração do access token (2h + 1min)
        with freeze_time("2025-06-15 10:01:00"):
            # Agora o token deve estar expirado
            expired_response = self.client.get(self.profile_url)
            self.assertEqual(expired_response.status_code, status.HTTP_401_UNAUTHORIZED)
