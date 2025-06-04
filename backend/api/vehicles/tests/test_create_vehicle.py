from rest_framework import status
from django.urls import reverse
from .vehicle_test_case import VehicleTestCase

class CreateVehicleTest(VehicleTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('vehicles:create_vehicle')

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
