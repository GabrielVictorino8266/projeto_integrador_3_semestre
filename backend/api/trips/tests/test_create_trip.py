from rest_framework import status
from django.urls import reverse
from .trips_test_case import TripsTestCase
from trips.models import Trip

class TestCreateTrip(TripsTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('trips:create_trip')

    def test_create_trip(self):
        response = self.client.post(self.url, self.valid_trip_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Trip.objects.count(), 1)
        self.assertEqual(Trip.objects.first().driverId, self.test_driver.id)