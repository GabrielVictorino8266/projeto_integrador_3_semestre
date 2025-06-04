from rest_framework.test import APITestCase
from users.authentication import SimpleUser
from vehicles.models import Vehicle, VehicleTypes
from mongoengine import connection


class VehicleTestCase(APITestCase):
    def setUp(self):
        self.db = connection.get_db()
        self.mock_user_data = {
            '_id': '507f1f77bcf86cd799439011',
            'email': 'test@example.com',
            'name': 'Test User',
            'role': 'user'
        }
        self.test_user = SimpleUser(self.mock_user_data)
        self.client.force_authenticate(user=self.test_user)

        self.valid_vehicle_data = {
            'numeroVeiculo': '12345',
            'placa': 'ABC1234',
            'tipoVeiculo': VehicleTypes.CARRO,
            'anoFabricacao': 2020,
            'marca': 'Fiat',
            'kmAtual': 50000,
            'limiteAvisoKm': 10000,
            'dataExclusao': None
        }

    def tearDown(self) -> None:
        self.db[Vehicle._get_collection_name()].drop()
        super().tearDown()
