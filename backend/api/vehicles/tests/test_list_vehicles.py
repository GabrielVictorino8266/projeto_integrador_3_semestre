from rest_framework import status
from django.urls import reverse
from .vehicle_test_case import VehicleTestCase
from vehicles.models import Vehicle


class ListVehiclesTest(VehicleTestCase):
    def setUp(self):
        """
        Configura o ambiente de teste criando múltiplos veículos válidos.
        """
        super().setUp()
        self.vehicles = [
            Vehicle.objects.create(**self.valid_vehicle_data),
            Vehicle.objects.create(**self.valid_vehicle_data),
        ]
        self.url = reverse('vehicles:list_vehicles')

    def test_list_vehicles_success(self):
        """
        Testa a recuperação bem-sucedida da lista de veículos.
        """
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.vehicles))
        
        # Verifica se ambos os veículos criados estão na resposta.
        response_ids = [v['id'] for v in response.data]
        for vehicle in self.vehicles:
            self.assertIn(str(vehicle.id), response_ids)

    def test_list_vehicles_unauthenticated(self):
        """
        Testa a tentativa de listar veículos sem autenticação.
        """
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)