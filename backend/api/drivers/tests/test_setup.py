from rest_framework.test import APITestCase
from rest_framework import status
from django.test import override_settings
from django.urls import reverse
from mongoengine import connect, disconnect
from bson import ObjectId
import mongomock
from datetime import datetime

from ..models import Driver
from ..views import get_hash_password
from users.auth_services import create_token
from users.authentication import SimpleUser

@override_settings(MONGO_DATABASE_NAME='testdb')
class BaseDriverTest(APITestCase):
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
        Driver.objects.delete()
        disconnect(alias='default')
        cls.mock_connection.close()
        super().tearDownClass()

    def setUp(self):
        # Delete all existing drivers to start fresh
        Driver.objects.delete()
        
        # Criar um ObjectId válido para o usuário de teste
        self.user_id = '507f1f77bcf86cd799439011'
        
        self.test_user_data = {
            '_id': ObjectId(self.user_id),
            'email': 'test@example.com',
            'name': 'Test User',
            'type': 'Motorista',
            'cpf': '88888888887',
            'password': '872000',
            'isActive': True
        }

        # Inserir usuário de teste no banco de dados
        db = self.mock_connection['testdb']
        db.users.insert_one(self.test_user_data)
        
        self.test_user = SimpleUser(self.test_user_data)

        # Criar token JWT com os campos necessários
        token_payload = {
            'user_id': str(self.test_user._id),
            'name': self.test_user.name,
            'cpf': self.test_user.cpf,
            'type': self.test_user.type,
            'email': self.test_user.email,
            'isActive': True
        }
        
        self.token = create_token(
            token_payload,
            token_type='access',
            expires_hours=2
        )

        # Configurar o cliente de teste para usar o token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        
        self.valid_driver_data = {
            'name': 'John Doe',
            'birthYear': '1990-01-01',
            'cpf': '12345678901',  # CPF válido
            'phone': '+55 31 8765-4321',
            'licenseType': 'B',
            'licenseNumber': '987654',
            'performance': 5,
            'isActive': True,
            'type': 'Motorista'
        }

    def tearDown(self):
        # Delete all drivers including the test driver
        Driver.objects.delete()

    def get_driver_url(self, driver_id):
        return reverse('drivers:get_driver', kwargs={'driver_id': str(driver_id)})

    def update_driver_url(self, driver_id):
        return reverse('drivers:update_driver', kwargs={'driver_id': str(driver_id)})

    def delete_driver_url(self, driver_id):
        return reverse('drivers:delete_driver', kwargs={'driver_id': str(driver_id)})