from rest_framework import status
from django.urls import reverse
from .vehicle_test_case import VehicleTestCase
from vehicles.models import Vehicle
from bson import ObjectId

class DeleteVehicleTest(VehicleTestCase):
    def setUp(self):
        super().setUp()
        self.vehicle = Vehicle.objects.create(**self.valid_vehicle_data)
        self.url = reverse('vehicles:delete_vehicle', args=[str(self.vehicle.id)])

    def test_delete_vehicle_success(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertIsNone(Vehicle.objects(id=self.vehicle.id).first())

    def test_delete_vehicle_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_vehicle_not_found(self):
        not_found_id = str(ObjectId())
        url = reverse('vehicles:delete_vehicle', args=[not_found_id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_vehicle_invalid_id(self):
        url = reverse('vehicles:delete_vehicle', args=["invalid-object-id"])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
