from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from users.authentication import SimpleUser
from vehicles.vehicle_types import VehicleTypes

class CreateVehicleTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.mock_user_data = {
            '_id': '507f1f77bcf86cd799439011',
            'email': 'test@example.com',
            'name': 'Test User',
            'role': 'user'
        }
        self.test_user = SimpleUser(self.mock_user_data)
        self.valid_vehicle_data = {
            'numeroVeiculo': '12345',
            'placa': 'ABC1234',
            'tipoVeiculo': VehicleTypes.CARRO,
            'anoFabricacao': 2020,
            'marca': 'Fiat',
            'kmAtual': 50000,
            'limiteAvisoKm': 10000
        }
        self.client.force_authenticate(user=self.test_user)
        self.url = reverse('create_vehicle')

    def test_create_vehicle_success(self):
        response = self.client.post(self.url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for field in self.valid_vehicle_data:
            self.assertEqual(response.data[field], self.valid_vehicle_data[field])

    def test_create_vehicle_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_vehicle_invalid_tipo_veiculo(self):
        invalid_data = self.valid_vehicle_data.copy()
        invalid_data['tipoVeiculo'] = 'invalid_choice'
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('tipoVeiculo', response.data)

    def test_create_vehicle_missing_required_fields(self):
        minimal_data = {'numeroVeiculo': '12345'}
        response = self.client.post(self.url, minimal_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
