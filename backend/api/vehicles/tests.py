from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .controller import create_vehicle

class VehicleControllerTest(TestCase):
    factory = APIRequestFactory()

    def test_create_vehicle(self):
        vehicle_data = {
            'numeroVeiculo': 'Ford',
            'placa': 'Mustang',
            'tipoVeiculo': 'red',
            'anoFabricacao': 2019,
            'marca': 'red',
            'kmAtual': 22000.0
        }

        request = self.factory.post('/api/vehicles/create/', vehicle_data, format='json')
        request.user = self.user
        response = create_vehicle(request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['numeroVeiculo'], vehicle_data['numeroVeiculo'])
        self.assertEqual(response.data['placa'], vehicle_data['placa'])
        self.assertEqual(response.data['tipoVeiculo'], vehicle_data['tipoVeiculo'])
        self.assertEqual(response.data['anoFabricacao'], vehicle_data['anoFabricacao'])
        self.assertEqual(response.data['marca'], vehicle_data['marca'])
        self.assertEqual(response.data['kmAtual'], vehicle_data['kmAtual'])