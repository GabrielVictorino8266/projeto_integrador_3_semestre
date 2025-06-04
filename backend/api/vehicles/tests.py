from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .controller import create_vehicle
from users.authentication import SimpleUser
from .vehicle_types import VehicleTypes

class VehicleControllerTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Dados de usuário simulados
        self.mock_user_data = {
            '_id': '507f1f77bcf86cd799439011',
            'email': 'test@example.com',
            'name': 'Test User',
            'role': 'user'
        }

        # Cria uma instância de SimpleUser para testes
        self.test_user = SimpleUser(self.mock_user_data)

    def test_create_vehicle(self):
        vehicle_data = {
            'numeroVeiculo': 'Ford',
            'placa': 'Mustang',
            'tipoVeiculo': VehicleTypes.CARRO,
            'anoFabricacao': 2019,
            'marca': 'red',
            'kmAtual': 22000.0,
            'limiteAvisoKm': 22000
        }

        self.client.force_authenticate(user=self.test_user)
        response = self.client.post('/api/vehicles/create/', vehicle_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['numeroVeiculo'], vehicle_data['numeroVeiculo'])
        self.assertEqual(response.data['placa'], vehicle_data['placa'])
        self.assertEqual(response.data['tipoVeiculo'], vehicle_data['tipoVeiculo'])
        self.assertEqual(response.data['anoFabricacao'], vehicle_data['anoFabricacao'])
        self.assertEqual(response.data['marca'], vehicle_data['marca'])
        self.assertEqual(response.data['kmAtual'], vehicle_data['kmAtual'])
        self.assertEqual(response.data['limiteAvisoKm'], vehicle_data['limiteAvisoKm'])