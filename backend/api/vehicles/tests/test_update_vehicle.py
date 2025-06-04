from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from vehicles.models import Vehicle
from vehicles.vehicle_types import VehicleTypes

class UpdateVehicleTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_vehicle_data = {
            'numeroVeiculo': '12345',
            'placa': 'ABC1234',
            'tipoVeiculo': VehicleTypes.CARRO,
            'anoFabricacao': 2020,
            'marca': 'Fiat',
            'kmAtual': 50000,
            'limiteAvisoKm': 10000
        }
        self.vehicle = Vehicle.objects.create(**self.valid_vehicle_data)
        self.url = reverse('update_vehicle', args=[str(self.vehicle.id)])

    def test_update_vehicle_success(self):
        response = self.client.put(self.url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for field in self.valid_vehicle_data:
            self.assertEqual(response.data[field], self.valid_vehicle_data[field])

    def test_update_vehicle_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.put(self.url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_vehicle_invalid_id(self):
        invalid_url = reverse('update_vehicle', args=['invalid_id'])
        response = self.client.put(invalid_url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_vehicle_invalid_data(self):
        invalid_data = {'numeroVeiculo': '12345', 'placa': 'INVALID'}
        response = self.client.put(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
