from .test_setup import BaseDriverTest
from rest_framework import status
from ..models import Driver

class TestDriverRetrieve(BaseDriverTest):
    def setUp(self):
        super().setUp()
        # Create a test driver for this specific test
        self.test_driver_data = {
            'name': 'Test Driver',
            'birthYear': '1990-01-01',
            'cpf': '22222222222',  # Different CPF
            'phone': '+55 31 7777-7777',
            'licenseType': 'B',
            'licenseNumber': '777777',
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

    def test_retrieve_driver_details(self):
        """Test retrieving driver details"""
        response = self.client.get(self.get_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], str(self.driver_id))
        self.assertEqual(response.data['name'], self.test_driver_data['name'])
        self.assertEqual(response.data['cpf'], self.test_driver_data['cpf'])
        self.assertEqual(response.data['type'], self.test_driver_data['type'])
        self.assertEqual(response.data['licenseType'], self.test_driver_data['licenseType'])
        self.assertEqual(response.data['licenseNumber'], self.test_driver_data['licenseNumber'])
        self.assertEqual(response.data['performance'], self.test_driver_data['performance'])
        self.assertTrue(response.data['isActive'])

    def test_retrieve_non_existent_driver(self):
        """Test retrieving a non-existent driver"""
        non_existent_id = '123456789012345678901234'
        response = self.client.get(self.get_driver_url(non_existent_id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_driver_with_invalid_id(self):
        """Test retrieving a driver with invalid ID format"""
        invalid_id = 'invalid-id-format'
        response = self.client.get(self.get_driver_url(invalid_id))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_non_existent_driver(self):
        """Test retrieving a non-existent driver"""
        non_existent_id = '123456789012345678901234'
        response = self.client.get(self.get_driver_url(non_existent_id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_deleted_driver(self):
        """Test retrieving a deleted driver"""
        # First delete the driver
        self.test_driver.delete()
        
        # Try to retrieve it
        response = self.client.get(self.get_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_inactive_driver(self):
        """Test retrieving an inactive driver"""
        # First deactivate the driver
        self.test_driver.isActive = False
        self.test_driver.save()
        
        # Retrieve the driver
        response = self.client.get(self.get_driver_url(self.driver_id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['isActive'])

    def test_retrieve_driver_with_invalid_id(self):
        """Test retrieving a driver with invalid ID format"""
        invalid_id = 'invalid-id-format'
        response = self.client.get(self.get_driver_url(invalid_id))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)