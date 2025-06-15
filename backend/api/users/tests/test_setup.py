from rest_framework.test import APITestCase
from django.conf import settings
from django.test import override_settings
from mongoengine import connect, disconnect
import mongomock
import json
import os

@override_settings(
    MONGO_DATABASE_NAME='testdb',
    SIMPLE_JWT={
        'ACCESS_TOKEN_LIFETIME_HOURS': 1,
        'REFRESH_TOKEN_LIFETIME_HOURS': 24,
        'ALGORITHM': 'HS256'
    }
)
class UsersTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        disconnect(alias='default')
        cls.mock_connection = connect(
            db='testdb',
            host='mongodb://localhost',
            alias='default',
            mongo_client_class=mongomock.MongoClient
        )

    @classmethod
    def tearDownClass(cls):
        disconnect(alias='default')
        cls.mock_connection.close()
        super().tearDownClass()

    def setUp(self):
        # Dados de usuário válido para testes
        self.valid_user_data = {
            "cpf": "12345678901",
            "password": "senha123",
            "name": "Test User",
            "type": "Motorista",
            "phone": "11999999999",
            "licenseType": "A",
            "licenseNumber": "123456",
            "birthYear": "2000-01-01",
            "performance": 10,
            "isActive": True
        }
        
        # Criar usuário de teste
        self.db = self.mock_connection.testdb
        self.db.users.insert_one(self.valid_user_data)
        
        # URLs comuns
        self.base_url = '/api/users/'
        self.login_url = f'{self.base_url}login/'
        self.refresh_url = f'{self.base_url}refresh-token/'
        self.logout_url = f'{self.base_url}logout/'
        self.profile_url = f'{self.base_url}profile/'

    def get_login_url(self):
        return self.login_url

    def get_refresh_url(self):
        return self.refresh_url

    def get_logout_url(self):
        return self.logout_url

    def get_profile_url(self):
        return self.profile_url

    def tearDown(self):
        # Limpar banco de teste
        self.db.users.delete_many({})
        self.db.refresh_tokens.delete_many({})
        self.db.blacklisted_tokens.delete_many({})
        self.db.users.delete_one({'cpf': self.valid_user_data['cpf']})

    def get_login_url(self):
        return self.login_url

    def get_refresh_url(self):
        return self.refresh_url

    def get_logout_url(self):
        return self.logout_url

    def get_profile_url(self):
        return self.profile_url
