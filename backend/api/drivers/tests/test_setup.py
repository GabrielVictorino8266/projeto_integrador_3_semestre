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