from users.authentication import SimpleUser
from drivers.models import Driver
from trips.models import Trip, TripStatus
from mongoengine import connection
from core.utils.mongo_test_case import MongoTestCase
from datetime import datetime, timezone
from vehicles.models import Vehicle, VehicleTypes

class TripsTestCase(MongoTestCase):
    def setUp(self):
        super().setUp()

        self.db = connection.get_db()
        self.mock_user_data = {
            '_id': '507f1f77bcf86cd799439011',
            'email': 'test@example.com',
            'name': 'Test User',
            'role': 'user'
        }
        self.test_user = SimpleUser(self.mock_user_data)
        self.client.force_authenticate(user=self.test_user)

        self.test_vehicle = Vehicle.objects.create(
            vehicleNumber='12345',
            licensePlate='ABC1234',
            vehicleType=VehicleTypes.CARRO,
            manufacturingYear=2020,
            brand='Fiat',
            currentKm=50000,
            warningKmLimit=10000
        )

        self.test_driver = Driver.objects.create(
            name='Test Driver',
            cpf='12345678901',
            birthYear='1990-01-01',
            phone='+55 31 6666-6666',
            licenseType='B',
            licenseNumber='666666',
            performance=5,
            isActive=True,
            type='Motorista'
        )

        self.valid_trip_data = {
            'vehicleId': self.test_vehicle.id,
            'driverId': self.test_driver.id,
            'startDateTime': datetime.now(timezone.utc),
            'endDateTime': datetime.now(timezone.utc),
            'origin': 'Origin',
            'destination': 'Destination',
            'initialKm': 50000,
            'finalKm': 60000,
            'completed': True,
            'status': TripStatus.ACTIVE
        }

    def tearDown(self) -> None:
        super().tearDown()
        Vehicle.objects.update(set__trips=[])