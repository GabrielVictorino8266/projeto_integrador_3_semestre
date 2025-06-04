from rest_framework import status
from django.urls import reverse
from .vehicle_test_case import VehicleTestCase
from vehicles.models import Vehicle
from bson import ObjectId

class DeleteVehicleTest(VehicleTestCase):
    def setUp(self):
        """
        Configura o ambiente de teste criando um veículo válido.
        """
        super().setUp()
        self.vehicle = Vehicle.objects.create(**self.valid_vehicle_data)
        self.url = reverse('vehicles:delete_vehicle', args=[str(self.vehicle.id)])

    def test_delete_vehicle_success(self):
        """
        Testa a exclusão bem-sucedida de um veículo existente.
        """
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        vehicle = Vehicle.objects(id=self.vehicle.id).first()
        self.assertIsNotNone(vehicle)
        self.assertIsNotNone(vehicle.dataExclusao)

    def test_delete_vehicle_unauthenticated(self):
        """
        Testa a tentativa de exclusão de um veículo sem autenticação.
        """
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_vehicle_not_found(self):
        """
        Testa a tentativa de exclusão de um veículo inexistente.
        """
        not_found_id = str(ObjectId())
        url = reverse('vehicles:delete_vehicle', args=[not_found_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_vehicle_invalid_id(self):
        """
        Testa a tentativa de exclusão de um veículo com ID inválido.
        """
        url = reverse('vehicles:delete_vehicle', args=["invalid-object-id"])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
