from .test_setup import BaseDriverTest
from rest_framework import status

class TestDriverUpdate(BaseDriverTest):
    def test_update_driver(self):
        """Test updating driver information"""
        update_data = {
            'name': 'John Doe Updated',
            'cpf': '12345678901',
            'phone': '+55 31 1234-5678',
            'licenseType': 'A',
            'licenseNumber': '123456',
            'performance': 5,
            'type': 'Motorista'
        }
        response = self.client.put(self.update_driver_url(self.driver_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_data['name'])
        self.assertEqual(response.data['cpf'], update_data['cpf'])
        self.assertEqual(response.data['phone'], update_data['phone'])
        self.assertEqual(response.data['licenseType'], update_data['licenseType'])
        self.assertEqual(response.data['licenseNumber'], update_data['licenseNumber'])
        self.assertEqual(response.data['performance'], update_data['performance'])
        self.assertEqual(response.data['type'], update_data['type'])