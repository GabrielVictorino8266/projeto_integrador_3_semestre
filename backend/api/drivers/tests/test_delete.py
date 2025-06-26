from .test_setup import BaseDriverTest
from rest_framework import status
from datetime import datetime
import time
from ..models import Driver

class TestDriverDelete(BaseDriverTest):
    def setUp(self):
        super().setUp()
        # Create a test driver for this specific test
        self.test_driver_data = {
            'name': 'Test Driver',
            'birthYear': '1990-01-01',
            'cpf': '11111111112',  # Different CPF from base
            'phone': '553188888888',
            'licenseType': 'B',
            'licenseNumber': '888888',
            'performance': 5,
            'isActive': True,
            'type': 'Motorista'
        }
        self.test_driver = Driver(**self.test_driver_data)
        self.test_driver.save()
        self.driver_id = str(self.test_driver.id)

    def tearDown(self):
        # Delete the test driver
        if hasattr(self, 'test_driver'):
            self.test_driver.delete()
        super().tearDown()

    def test_delete_driver(self):
        """Test deleting driver"""
        # First get the driver to confirm it exists
        response = self.client.get(self.get_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Now delete the driver
        response = self.client.delete(self.delete_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify driver is marked as inactive
        response = self.client.get(self.get_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['isActive'])

    def test_delete_non_existent_driver(self):
        """Test deleting a non-existent driver"""
        non_existent_id = '12345678bjkbkkjh9012345678901234'  # Invalid ID
        response = self.client.delete(self.delete_driver_url(non_existent_id))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_driver_with_incidents(self):
        """Test deleting a driver with incidents"""
        # Add incidents to the driver
        self.test_driver.incidents = ['incident1', 'incident2']
        self.test_driver.save()

        # Delete the driver
        response = self.client.delete(self.delete_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify incidents are preserved
        response = self.client.get(self.get_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['incidents']), 2)

    def test_soft_delete_behavior(self):
        """Test that soft delete doesn't actually remove the driver from database"""
        # Delete the driver
        response = self.client.delete(self.delete_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Verify driver still exists in database
        driver = Driver.objects.get(id=self.driver_id)
        self.assertIsNotNone(driver)
        self.assertTrue(driver.deleted)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)