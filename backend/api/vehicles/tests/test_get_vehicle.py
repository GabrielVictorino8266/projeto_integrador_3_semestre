from rest_framework import status
from django.urls import reverse
from .vehicle_test_case import VehicleTestCase
from vehicles.models import Vehicle
from bson import ObjectId

class GetVehicleTest(VehicleTestCase):
    def setUp(self):
        """
        Configura o ambiente de teste criando um veículo válido.
        """
        super().setUp()
        self.vehicle = Vehicle.objects.create(**self.valid_vehicle_data)
        self.url = reverse('vehicles:get_vehicle', args=[str(self.vehicle.id)])

    def test_get_vehicle_success(self):
        """
        Testa a recuperação bem-sucedida de um veículo existente.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.vehicle.id))

    def test_get_vehicle_not_found(self):
        """
        Testa a tentativa de recuperação de um veículo inexistente.
        """
        not_found_id = str(ObjectId())
        url = reverse('vehicles:get_vehicle', args=[not_found_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_vehicle_invalid_id(self):
        """
        Testa a tentativa de recuperação de um veículo com ID inválido.
        """
        url = reverse('vehicles:get_vehicle', args=["id-invalido"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)