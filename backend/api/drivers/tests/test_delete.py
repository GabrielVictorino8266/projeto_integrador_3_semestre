from .test_setup import BaseDriverTest
from rest_framework import status

class TestDriverDelete(BaseDriverTest):
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
        self.assertFalse(response.data['isActive'])