from rest_framework import status
from .test_setup import UsersTestCase
from freezegun import freeze_time

class LogoutTest(UsersTestCase):
    def setUp(self):
        super().setUp()
        self.logout_url = self.get_logout_url()
        self.login_url = self.get_login_url()
        self.profile_url = self.get_profile_url()

    @freeze_time("2025-06-15 08:00:00")
    def test_logout_success(self):
        """
        Testa o logout com sucesso usando refresh token válido.
        """
        # Primeiro faz login para obter refresh token
        login_response = self.client.post(self.login_url, {
            'cpf': self.valid_user_data['cpf'],
            'password': self.plain_password
        }, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        
        access_token = login_response.data['access_token']
        refresh_token = login_response.data['refresh_token']
        
        # Agora tenta logout
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        logout_response = self.client.post(self.logout_url, {
            'refresh_token': refresh_token
        }, format='json')
        
        self.assertEqual(logout_response.status_code, status.HTTP_200_OK)
        self.assertEqual(logout_response.data['detail'], 'Logout realizado com sucesso.')
        
        # Verifica que o refresh token foi invalidado
        refresh_response = self.client.post(self.refresh_url, {
            'refresh_token': refresh_token
        }, format='json')
        self.assertEqual(refresh_response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Avança o tempo em 1 hora para garantir que o token de acesso expirou
        with freeze_time("2025-06-15 10:01:00"):
            # Testa token de acesso expirado
            profile_response = self.client.get(self.profile_url)
            self.assertEqual(profile_response.status_code, status.HTTP_401_UNAUTHORIZED)



    def test_logout_missing_token(self):
        """
        Testa tentativa de logout sem token.
        """
        # First get a valid token
        login_response = self.client.post(self.login_url, {
            'cpf': self.valid_user_data['cpf'],
            'password': self.plain_password
        }, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        access_token = login_response.data['access_token']
        
        # Try logout without refresh token but with valid access token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        response = self.client.post(self.logout_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'Refresh Token é necessário, verifique-o e envie novamente.')

    def test_logout_invalid_token(self):
        """
        Testa tentativa de logout com token inválido.
        """
        # Primeiro faz login para obter um token válido
        login_response = self.client.post(self.login_url, {
            'cpf': self.valid_user_data['cpf'],
            'password': self.plain_password
        }, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        
        # Agora tenta logout com token inválido
        response = self.client.post(self.logout_url, {
            'refresh_token': 'invalid_token'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_already_invalidated_token(self):
        """
        Testa tentativa de logout com token já invalidado.
        """
        # Primeiro faz login para obter refresh token
        login_response = self.client.post(self.login_url, {
            'cpf': self.valid_user_data['cpf'],
            'password': self.plain_password
        }, format='json')
        self.assertEqual(login_response.status_code, status.HTTP_200_OK)
        
        refresh_token = login_response.data['refresh_token']
        access_token = login_response.data['access_token']
        
        # Primeiro logout
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        first_logout = self.client.post(self.logout_url, {
            'refresh_token': refresh_token
        }, format='json')
        self.assertEqual(first_logout.status_code, status.HTTP_200_OK)
        
        # Segundo logout
        second_logout = self.client.post(self.logout_url, {
            'refresh_token': refresh_token
        }, format='json')
        self.assertEqual(second_logout.status_code, status.HTTP_401_UNAUTHORIZED)
