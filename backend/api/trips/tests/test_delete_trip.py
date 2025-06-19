from rest_framework import status
from django.urls import reverse
from bson import ObjectId
from .trips_test_case import TripsTestCase
from vehicles.models import Vehicle
from trips.models import Trip
from datetime import datetime, timezone, timedelta
from trips.models import TripStatus

class DeleteTripTest(TripsTestCase):
    def setUp(self):
        super().setUp()
        
        # Criar uma viagem para teste
        self.trip = Trip(
            driverId=self.test_driver.id,
            startDateTime=datetime.now(timezone.utc),
            endDateTime=datetime.now(timezone.utc) + timedelta(hours=4),
            origin="Origin",
            destination="Destination",
            initialKm=1000,
            finalKm=1100,
            completed=True,
            status=TripStatus.ACTIVE
        )
        self.test_vehicle.trips.append(self.trip)
        self.test_vehicle.save()
        
        self.trip_id = str(self.trip.id)
        self.url = reverse('trips:delete_trip', args=[self.trip_id])

    def test_delete_trip_success(self):
        """
        Testa a exclusão bem-sucedida de uma viagem.
        """
        response = self.client.delete(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verificar se a viagem foi marcada como deletada
        vehicle = Vehicle.objects.get(id=self.test_vehicle.id)
        trip = next((t for t in vehicle.trips if str(t.id) == self.trip_id), None)
        self.assertTrue(trip.deleted)
        self.assertIsNotNone(trip.deletedAt)

    def test_delete_nonexistent_trip(self):
        """
        Testa a tentativa de excluir uma viagem que não existe.
        """
        non_existent_id = '60f7f5e9e1d2f123456789ab'
        url = reverse('trips:delete_trip', args=[non_existent_id])
        
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('Viagem não encontrada', str(response.data))

    def test_delete_twice(self):
        """
        Testa a tentativa de excluir uma viagem já excluída.
        """
        # Primeira exclusão
        self.client.delete(self.url)
        
        # Segunda tentativa
        response = self.client.delete(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('Viagem não encontrada', str(response.data))