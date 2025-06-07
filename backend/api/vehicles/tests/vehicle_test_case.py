from rest_framework.test import APITestCase
from users.authentication import SimpleUser
from vehicles.models import Vehicle, VehicleTypes
from mongoengine import connection, connect, disconnect
from mongoengine import connect, disconnect
from mongomock import MongoClient

class MongoTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Conecta a uma instância MongoDB em memória usando mongomock
        disconnect(alias='default')
        connect(mongo_client_class=MongoClient)

    @classmethod
    def tearDownClass(cls):
        # Desconecta da instância MongoDB mockada
        disconnect(alias='testdb')
        super().tearDownClass()


class VehicleTestCase(MongoTestCase):
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
            'vehicleNumber': '12345',
            'licensePlate': 'ABC1234',
            'vehicleType': VehicleTypes.CARRO,
            'manufacturingYear': 2020,
            'brand': 'Fiat',
            'currentKm': 50000,
            'warningKmLimit': 10000,
            'deletedAt': None
        }

    def tearDown(self) -> None:
        self.db[Vehicle._get_collection_name()].drop()
        super().tearDown()
