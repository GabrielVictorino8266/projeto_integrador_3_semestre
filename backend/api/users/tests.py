from rest_framework.test import APITestCase
from rest_framework import status

class TestLoginController(APITestCase):
    def test_login_sucess(self):
        user_data = {
            "cpf": "18092754314",
            "password": "1996180"
        }
        response = self.client.post('/api/users/login/', user_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.data)

    def test_login_invalid_credentials(self):
        user_data = {
            "cpf": "invaliduser",
            "password": "wrongpassword"
        }
        response = self.client.post('/api/users/login/', user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_login_missing_fields(self):
        user_data = {
            "cpf": "testuser"
        }
        response = self.client.post('/api/users/login/', user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)