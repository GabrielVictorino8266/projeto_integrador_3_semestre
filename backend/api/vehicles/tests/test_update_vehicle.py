from rest_framework import status
from django.urls import reverse
from .vehicle_test_case import VehicleTestCase
from vehicles.models import Vehicle
from bson import ObjectId

class UpdateVehicleTest(VehicleTestCase):
    def setUp(self):
        """
        Configura o ambiente de teste criando um veículo válido.
        """
        super().setUp()
        self.vehicle = Vehicle.objects.create(**self.valid_vehicle_data)
        self.url = reverse('vehicles:update_vehicle', args=[str(self.vehicle.id)])

    def test_update_vehicle_success(self):
        """
        Testa a atualização bem-sucedida de um veículo existente.
        """
        response = self.client.put(self.url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for field in self.valid_vehicle_data:
            self.assertEqual(response.data[field], self.valid_vehicle_data[field])

    def test_update_vehicle_unauthenticated(self):
        """
        Testa a tentativa de atualização sem autenticação.
        """
        self.client.force_authenticate(user=None)
        response = self.client.put(self.url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_vehicle_invalid_id(self):
        """
        Testa a tentativa de atualização com ID inexistente.
        """
        invalid_url = reverse('vehicles:update_vehicle', args=[str(ObjectId())])
        response = self.client.put(invalid_url, self.valid_vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_vehicle_invalid_data(self):
        """
        Testa a tentativa de atualização com dados inválidos.
        """
        invalid_data = {'numeroVeiculo': '12345', 'placa': 'INVALID'}
        response = self.client.put(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
