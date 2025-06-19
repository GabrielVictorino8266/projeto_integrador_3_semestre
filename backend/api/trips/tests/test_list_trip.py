from rest_framework import status
from django.urls import reverse
from .trips_test_case import TripsTestCase
from vehicles.models import Vehicle
from trips.models import Trip, TripStatus
from datetime import datetime, timedelta, timezone

class ListTripsTest(TripsTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('trips:list_trips')
        
        # Criar algumas viagens de teste
        self.trips = []
        for i in range(3):
            trip = Trip(
                driverId=self.test_driver.id,
                startDateTime=datetime.now(timezone.utc) - timedelta(days=i),
                endDateTime=datetime.now(timezone.utc) - timedelta(days=i) + timedelta(hours=4),
                origin=f"Origin {i}",
                destination=f"Destination {i}",
                initialKm=1000 * (i + 1),
                finalKm=1100 * (i + 1),
                completed=True,
                status=TripStatus.ACTIVE
            )
            self.test_vehicle.trips.append(trip)
            self.trips.append(trip)
        self.test_vehicle.save()

    def test_list_trips_success(self):
        """
        Testa a listagem bem-sucedida de viagens.
        """
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total'], 3)
        self.assertEqual(len(response.data['items']), 3)
        
        # Verificar se os dados básicos estão corretos
        for i, trip in enumerate(self.trips):  # Ordem decrescente por data
            trip_data = response.data['items'][i]
            self.assertEqual(trip_data['origin'], f"Origin {i}")
            self.assertEqual(trip_data['destination'], f"Destination {i}")

    def test_list_trips_pagination(self):
        """
        Testa a paginação na listagem de viagens.
        """
        response = self.client.get(f"{self.url}?page=1&limit=2")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total'], 3)
        self.assertEqual(len(response.data['items']), 2)
        self.assertEqual(response.data['current_page'], 1)
        self.assertEqual(response.data['per_page'], 2)
        self.assertEqual(response.data['last_page'], 2)

    def test_list_trips_filter_by_destination(self):
        """
        Testa a filtragem de viagens por destino.
        """
        response = self.client.get(f"{self.url}?destination=Destination 1")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total'], 1)
        self.assertEqual(response.data['items'][0]['destination'], "Destination 1")