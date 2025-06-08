from rest_framework.test import APITestCase
from rest_framework import status
from django.test import override_settings
from django.urls import reverse
from mongoengine import connect, disconnect
from bson import ObjectId
import mongomock

from .models import Driver

@override_settings(MONGO_DATABASE_NAME='testdb')
class DriverAPITests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Desconecta se já houver conexão com o alias 'default'
        disconnect(alias='default')
        # Conecta ao banco fake com mongomock
        cls.mock_connection = connect(
            db='testdb',
            host='mongodb://localhost',
            alias='default',
            mongo_client_class=mongomock.MongoClient
        )

    @classmethod
    def tearDownClass(cls):
        disconnect(alias='default')
        super().tearDownClass()

    def setUp(self):
        # Cria driver fictício
        self.driver = Driver.objects.create(
            name='Teste',
            email='teste@example.com',
            password='Teste123',
            birthYear="1990-01-01",
            cpf='12345678900',
            phone='+55 31 1234-5678',
            licenseType='A',
            licenseNumber='ABC1234',
            performance=7,
            isActive=True,
            type='Motorista'
        )

    def test_get_drivers(self):
        url = reverse('drivers:list_drivers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Teste', str(response.data))

    def test_create_driver(self):
        # Test POST /drivers/
        data = {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'password': 'password123',
            'cpf': '98765432109',
            'phone': '+55 31 8765-4321',
            'birthYear':"1990-01-01",
            'licenseType': 'B',
            'licenseNumber': '987654',
            'performance': 5,
            'isActive': True,
            'type': 'Motorista'
        }
        response = self.client.post(reverse('drivers:create_driver'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Driver.objects.count(), 2)

    def test_retrieve_driver_details(self):
        # Test GET /drivers/<id>/
        response = self.client.get(reverse('drivers:get_driver', kwargs={'driver_id': str(self.driver.id)}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.driver.name)

    def test_update_driver(self):
        # Test PUT /drivers/<id>/
        data = {
            'name': 'John Doe Updated',
            'email': 'john.updated@example.com',
            'password': 'password123',
            'cpf': '12345678901',
            'phone': '+55 31 1234-5678',
            'licenseType': 'A',
            'licenseNumber': '123456',
            'performance': 5,
            'isActive': True,
            'type': 'Motorista'
        }
        response = self.client.put(reverse('drivers:update_driver', kwargs={'driver_id': str(self.driver.id)}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.driver.reload()
        self.assertEqual(self.driver.name, 'John Doe Updated')

    def test_delete_driver(self):
        # Test DELETE /drivers/<id>/
        response = self.client.delete(reverse('drivers:delete_driver', kwargs={'driver_id': str(self.driver.id)}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)