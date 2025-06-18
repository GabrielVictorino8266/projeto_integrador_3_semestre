from rest_framework import status
from django.urls import reverse
from .trips_test_case import TripsTestCase
from datetime import datetime, timezone, timedelta
from bson import ObjectId
from trips.models import Trip

class UpdateTripTest(TripsTestCase):
    def setUp(self):
        super().setUp()
        # Cria uma viagem vinculada ao veículo de teste
        self.test_vehicle.trips.append(Trip(**self.valid_trip_data))
        self.test_vehicle.save()
        self.trip = self.test_vehicle.trips[-1]
        self.url = reverse('trips:update_trip', args=[str(self.trip.id)])

    def test_update_trip_success(self):
        """
        Testa a atualização bem-sucedida de uma viagem existente.
        """
        end_time = datetime.now(timezone.utc) + timedelta(hours=1)
        new_data = {
            'destination': 'Novo Destino',
            'completed': True,
            'endDateTime': end_time.isoformat()
        }
        response = self.client.put(self.url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data.get('destination'), new_data['destination'])
        self.assertEqual(response.data.get('completed'), new_data['completed'])
        self.assertAlmostEqual(
            datetime.fromisoformat(response.data.get('endDateTime')),
            datetime.fromisoformat(new_data['endDateTime']), 
            delta=timedelta(seconds=1)
        )

    def test_update_trip_unauthenticated(self):
        """
        Testa a tentativa de atualização sem autenticação.
        """
        self.client.force_authenticate(user=None)
        response = self.client.put(self.url, self.valid_trip_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_trip_invalid_id(self):
        """
        Testa a tentativa de atualização com ID inexistente.
        """
        invalid_url = reverse('trips:update_trip', args=[str(ObjectId())])
        response = self.client.put(invalid_url, self.valid_trip_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_trip_invalid_data(self):
        """
        Testa a tentativa de atualização com dados inválidos.
        """
        invalid_data = {'finalKm': -100}
        response = self.client.put(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
