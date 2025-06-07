from rest_framework import status
from django.urls import reverse
from .vehicle_test_case import VehicleTestCase

class CreateVehicleTest(VehicleTestCase):
    def setUp(self):
        """
        Configura o ambiente de teste, preparando a URL para criação de veículo.
        """
        super().setUp()
        self.url = reverse('vehicles:create_vehicle')

    def test_create_vehicle_success(self):
        """
        Testa a criação bem-sucedida de um veículo com dados válidos.
        """
        response = self.client.post(self.url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for field in self.valid_vehicle_data:
            self.assertEqual(response.data[field], self.valid_vehicle_data[field])

    def test_create_vehicle_unauthenticated(self):
        """
        Testa a tentativa de criação de um veículo sem autenticação.
        """
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_vehicle_invalid_tipo_veiculo(self):
        """
        Testa a criação de um veículo com tipo de veículo inválido.
        """
        invalid_data = self.valid_vehicle_data.copy()
        invalid_data['vehicleType'] = 'invalid_choice'
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('vehicleType', response.data)

    def test_create_vehicle_missing_required_fields(self):
        """
        Testa a criação de um veículo com campos obrigatórios ausentes.
        """
        minimal_data = {'vehicleNumber': '12345'}
        response = self.client.post(self.url, minimal_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
