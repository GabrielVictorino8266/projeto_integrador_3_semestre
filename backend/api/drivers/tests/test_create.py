from .test_setup import BaseDriverTest
from rest_framework import status
from django.urls import reverse
from ..models import Driver
import time
import concurrent.futures
import random
import string

class TestDriverCreate(BaseDriverTest):
    def test_create_valid_driver(self):
        """Test creating a driver with valid data"""
        data = {
            'name': 'Jane Smith',
            'birthYear': '1985-05-15',
            'cpf': '98765432109',  # Different CPF
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
        self.assertEqual(response.data['cpf'], data['cpf'])

    def test_create_driver_with_invalid_cpf(self):
        """Test creating a driver with invalid CPF"""
        data = self.valid_driver_data.copy()
        data['cpf'] = '1234567890'  # Invalid CPF format
        response = self.client.post(reverse('drivers:create_driver'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('This value does not match the required pattern.', str(response.data['cpf'][0]))

    def test_create_driver_with_missing_required_fields(self):
        """Test creating a driver with missing required fields"""
        required_fields = ['name', 'cpf', 'birthYear', 'phone', 'licenseType', 'licenseNumber']
        for field in required_fields:
            data = self.valid_driver_data.copy()
            del data[field]
            response = self.client.post(reverse('drivers:create_driver'), data, format='json')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(field, response.data)

    def test_create_driver_with_duplicate_cpf(self):
        """Test creating a driver with duplicate CPF"""
        # Create first driver with unique CPF
        data = self.valid_driver_data.copy()
        data['cpf'] = '98765432111'  # First unique CPF
        response = self.client.post(reverse('drivers:create_driver'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Try to create second driver with same CPF
        response = self.client.post(reverse('drivers:create_driver'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('cpf', response.data)

    def test_response_format(self):
        """Test response format and field types"""
        response = self.client.post(reverse('drivers:create_driver'), self.valid_driver_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verify all expected fields are present
        expected_fields = ['id', 'name', 'cpf', 'birthYear', 'phone', 'licenseType', 
                         'licenseNumber', 'performance', 'isActive', 'type']
        
        for field in expected_fields:
            self.assertIn(field, response.data)
        
        # Verify field types
        self.assertIsInstance(response.data['id'], str)
        self.assertIsInstance(response.data['cpf'], str)
        self.assertIsInstance(response.data['birthYear'], str)  # Assuming birthYear is stored as string

    def test_create_with_invalid_birth_year_format(self):
        """Test creating driver with invalid birth year format"""
        data = self.valid_driver_data.copy()
        data['birthYear'] = 'invalid-date'  # Invalid date format
        response = self.client.post(reverse('drivers:create_driver'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('birthYear', response.data)

    def test_create_with_invalid_performance_value(self):
        """Test creating driver with invalid performance value"""
        data = self.valid_driver_data.copy()
        data['performance'] = 11  # Invalid performance (should be 1-10)
        response = self.client.post(reverse('drivers:create_driver'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('performance', response.data)