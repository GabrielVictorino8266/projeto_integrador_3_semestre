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
        self.vehicle_count = 30
        self.vehicles = [
            Vehicle.objects.create(**self.valid_vehicle_data)
            for _ in range(self.vehicle_count)
        ]
        self.url = reverse('vehicles:list_vehicles')

    def test_list_vehicles_success(self):
        """
        Testa a recuperação bem-sucedida da lista de veículos.
        """
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), self.vehicle_count)
        
        response_ids = [v['id'] for v in response.data]
        for vehicle in self.vehicles:
            self.assertIn(str(vehicle.id), response_ids)

    def test_list_vehicles_pagination(self):
        """
        Testa a paginação com parâmetros de página e limite.
        """
        page = 2
        limit = 10
        response = self.client.get(self.url, {'page': page, 'limit': limit})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), limit)
        
        # Verifica se a página correta foi retornada
        expected_vehicles = self.vehicles[(page - 1) * limit: page * limit]
        response_ids = [v['id'] for v in response.data['data']]
        
        for vehicle in expected_vehicles:
            self.assertIn(str(vehicle.id), response_ids)

    def test_list_vehicles_unauthenticated(self):
        """
        Testa a tentativa de listar veículos sem autenticação.
        """
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
