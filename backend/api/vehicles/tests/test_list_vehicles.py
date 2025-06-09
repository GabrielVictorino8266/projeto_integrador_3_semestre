from rest_framework import status
from django.urls import reverse
from vehicles.models import Vehicle
from vehicles.types import VehicleStatus
from .vehicle_test_case import VehicleTestCase


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
        self.assertIn('items', response.data)
        self.assertEqual(len(response.data['items']), self.vehicle_count)
        
        response_ids = [v['id'] for v in response.data['items']]
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
        self.assertIn('items', response.data)
        self.assertEqual(len(response.data['items']), limit)
        
        # Verifica se a página correta foi retornada
        expected_vehicles = self.vehicles[(page - 1) * limit: page * limit]
        response_ids = [v['id'] for v in response.data['items']]
        
        for vehicle in expected_vehicles:
            self.assertIn(str(vehicle.id), response_ids)

    def test_list_vehicles_unauthenticated(self):
        """
        Testa a tentativa de listar veículos sem autenticação.
        """
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_vehicles_filter_by_status(self):
        """
        Testa a filtragem de veículos por status.
        """
        Vehicle.objects.create(**(self.valid_vehicle_data | {'status': VehicleStatus.INACTIVE}))
        response = self.client.get(self.url, {'status': VehicleStatus.ACTIVE})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('items', response.data)
        self.assertEqual(len(response.data['items']), self.vehicle_count)
        
        response_ids = [v['id'] for v in response.data['items']]
        for vehicle in self.vehicles:
            self.assertIn(str(vehicle.id), response_ids)

    def test_list_vehicles_filter_by_license_plate(self):
        """
        Testa a filtragem de veículos por placa com substring.
        """
        test_vehicle = Vehicle.objects.create(**(self.valid_vehicle_data | {'licensePlate': 'CDE1234'}))
        response = self.client.get(self.url, {'licensePlate': test_vehicle.licensePlate[:3]})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('items', response.data)
        self.assertEqual(len(response.data['items']), 1)
        
        response_ids = [v['id'] for v in response.data['items']]
        self.assertIn(str(test_vehicle.id), response_ids)