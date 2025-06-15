from .test_setup import BaseDriverTest
from rest_framework import status
from ..models import Driver

class TestDriverUpdate(BaseDriverTest):
    def setUp(self):
        super().setUp()
        # Create a test driver for this specific test
        self.test_driver_data = {
            'name': 'Test Driver',
            'birthYear': '1990-01-01',
            'cpf': '33333333333',  # Different CPF
            'phone': '+55 31 6666-6666',
            'licenseType': 'B',
            'licenseNumber': '666666',
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

    def test_update_driver(self):
        """Test updating driver information"""
        update_data = {
            'name': 'John Doe Updated',
            'cpf': '33333333333',  # Using the same CPF as test driver
            'birthYear': '1990-01-01',
            'phone': '+55 31 1234-5678',
            'licenseType': 'A',
            'licenseNumber': '123456',
            'performance': 5,
            'type': 'Motorista'
        }
        response = self.client.put(self.update_driver_url(self.driver_id), update_data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_data['name'])
        self.assertEqual(response.data['cpf'], update_data['cpf'])
        self.assertEqual(response.data['birthYear'], update_data['birthYear'])
        self.assertEqual(response.data['phone'], update_data['phone'])
        self.assertEqual(response.data['licenseType'], update_data['licenseType'])
        self.assertEqual(response.data['licenseNumber'], update_data['licenseNumber'])
        self.assertEqual(response.data['performance'], update_data['performance'])
        self.assertEqual(response.data['type'], update_data['type'])

    def test_update_driver_partial(self):
        """Test partial update of driver information"""
        update_data = {
            'name': 'John Doe Updated',
            'phone': '+55 31 1234-5678'
        }
        response = self.client.patch(self.update_driver_url(self.driver_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], update_data['name'])
        self.assertEqual(response.data['phone'], update_data['phone'])
        # Verify other fields remain unchanged
        self.assertEqual(response.data['cpf'], self.test_driver_data['cpf'])
        self.assertEqual(response.data['licenseType'], self.test_driver_data['licenseType'])

    def test_update_driver_invalid_data(self):
        """Test updating driver with invalid data"""
        update_data = {
            'cpf': 'invalid-cpf',  # Invalid CPF format
            'phone': 'invalid-phone',  # Invalid phone format
            'licenseType': 'X',  # Invalid license type
            'performance': 11  # Invalid performance (should be 1-10)
        }
        response = self.client.put(self.update_driver_url(self.driver_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_non_existent_driver(self):
        """Test updating non-existent driver"""
        non_existent_id = '123456789012345678901234'
        update_data = {'name': 'Should Not Work'}
        response = self.client.put(self.update_driver_url(non_existent_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_driver_invalid_id(self):
        """Test updating driver with invalid ID format"""
        invalid_id = 'invalid-id-format'
        update_data = {'name': 'Should Not Work'}
        response = self.client.put(self.update_driver_url(invalid_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_driver_performance(self):
        """Test updating driver performance"""
        update_data = {
            'performance': 8
        }
        response = self.client.patch(self.update_driver_url(self.driver_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['performance'], 8)

    def test_update_driver_name(self):
        """Test updating driver name"""
        update_data = {
            'name': 'New Driver Name'
        }
        response = self.client.patch(self.update_driver_url(self.driver_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'New Driver Name')

    def test_update_driver_phone(self):
        """Test updating driver phone number"""
        update_data = {
            'phone': '+55 31 9999-9999'
        }
        response = self.client.patch(self.update_driver_url(self.driver_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['phone'], '+55 31 9999-9999')

    def test_update_driver_license(self):
        """Test updating driver license information"""
        update_data = {
            'licenseType': 'C',
            'licenseNumber': '999999'
        }
        response = self.client.patch(self.update_driver_url(self.driver_id), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['licenseType'], 'C')
        self.assertEqual(response.data['licenseNumber'], '999999')