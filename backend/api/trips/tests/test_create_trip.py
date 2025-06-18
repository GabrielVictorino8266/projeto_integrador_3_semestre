from rest_framework import status
from django.urls import reverse
from .trips_test_case import TripsTestCase
from vehicles.models import Vehicle


class CreateTripTest(TripsTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('trips:create_trip')

    def test_create_trip_success(self):
        """
        Testa a criação bem-sucedida de uma viagem.
        """
        valid_data = self.valid_trip_data.copy()
        valid_data['vehicleId'] = str(self.test_vehicle.id)
        
        response = self.client.post(self.url, valid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        updated_vehicle = Vehicle.objects.get(id=self.test_vehicle.id)
        self.assertEqual(len(updated_vehicle.trips), 1)
        self.assertIsNotNone(response.data.get('id'))

    def test_create_trip_invalid_vehicle_id_format(self):
        """
        Testa a criação de uma viagem com ID de veículo mal formatado (inválido).
        Deve retornar 400.
        """
        invalid_data = self.valid_trip_data.copy()
        invalid_data['vehicleId'] = 'invalid_id_format'

        response = self.client.post(self.url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('ID do veículo inválido', str(response.data))

    def test_create_trip_vehicle_not_found(self):
        """
        Testa a criação de uma viagem com um veículo que não existe.
        """
        invalid_data = self.valid_trip_data.copy()
        invalid_data['vehicleId'] = '60f7f5e9e1d2f123456789ab'  # ID válido no formato, mas não existente

        response = self.client.post(self.url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('Veículo não encontrado', str(response.data))

    def test_create_trip_with_invalid_trip_data(self):
        """
        Testa criação de viagem com dados inválidos (ex: destino vazio).
        """
        invalid_data = self.valid_trip_data.copy()
        invalid_data['vehicleId'] = str(self.test_vehicle.id)
        invalid_data['destination'] = ''

        response = self.client.post(self.url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('destination', response.data)
