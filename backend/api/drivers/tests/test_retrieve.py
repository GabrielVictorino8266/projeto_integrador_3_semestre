from .test_setup import BaseDriverTest
from rest_framework import status

class TestDriverRetrieve(BaseDriverTest):
    def test_retrieve_driver_details(self):
        """Test retrieving driver details"""
        response = self.client.get(self.get_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.driver_id))
        self.assertEqual(response.data['name'], self.valid_driver_data['name'])
        self.assertEqual(response.data['cpf'], self.valid_driver_data['cpf'])
        self.assertEqual(response.data['type'], self.valid_driver_data['type'])