from rest_framework import status
from .test_setup import UsersTestCase

class LoginTest(UsersTestCase):
    def setUp(self):
        """
        Configura o ambiente de teste, preparando a URL para login e dados de teste.
        """
        super().setUp()

    def test_login_success(self):
        """
        Testa o login bem-sucedido com credenciais válidas.
        """
        response = self.client.post(self.get_login_url(), {
            'cpf': self.valid_user_data['cpf'],
            'password': self.plain_password
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access_token', response.data)
        self.assertIn('refresh_token', response.data)
        self.assertIn('user', response.data)
        
    def test_login_invalid_credentials(self):
        """
        Testa a tentativa de login com credenciais inválidas.
        """
        invalid_user_data = {
            "cpf": "18092754314",
            "password": "1996180"
        }
        response = self.client.post(self.get_login_url(), invalid_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_login_missing_required_fields(self):
        """
        Testa a tentativa de login com campos obrigatórios ausentes.
        """
        response = self.client.post(self.get_login_url(), {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_login_empty_credentials(self):
        """
        Testa a tentativa de login com credenciais vazias.
        """
        empty_user_data = {
            "cpf": "",
            "password": ""
        }
        response = self.client.post(self.get_login_url(), empty_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_login_nonexistent_user(self):
        """
        Testa a tentativa de login com usuário que não existe.
        """
        nonexistent_user_data = {
            "cpf": "12345678901", 
            "password": "somepassword"
        }
        response = self.client.post(self.get_login_url(), nonexistent_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)