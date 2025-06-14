from .test_setup import BaseDriverTest
from rest_framework import status
from django.urls import reverse

class TestDriverCreate(BaseDriverTest):
    def test_create_valid_driver(self):
        """Test creating a driver with valid data"""
        data = {
            'name': 'Jane Smith',
            'birthYear': '1985-05-15',
            'cpf': '12345678901',
            'phone': '+55 31 9876-5432',
            'licenseType': 'A',
            'licenseNumber': '123456',
            'performance': 4,
            'isActive': True,
            'type': 'Motorista'
        }
        response = self.client.post(reverse('drivers:create_driver'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)

    def test_create_driver_with_invalid_cpf(self):
        """Test creating a driver with invalid CPF"""
        data = self.valid_driver_data.copy()
        data['cpf'] = '1234567890'  # Invalid CPF format
        response = self.client.post(reverse('drivers:create_driver'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('cpf', response.data)

    def test_create_driver_with_missing_required_fields(self):
        """Test creating a driver with missing required fields"""
        data = self.valid_driver_data.copy()
        del data['name']  # Remove required field
        response = self.client.post(reverse('drivers:create_driver'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)