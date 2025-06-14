# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.test import override_settings
# from django.urls import reverse
# from mongoengine import connect, disconnect
# from bson import ObjectId
# import mongomock
# from datetime import datetime

# from .models import Driver
# from .views import get_hash_password

# @override_settings(MONGO_DATABASE_NAME='testdb')
# class DriverAPITests(APITestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         disconnect(alias='default')
#         cls.mock_connection = connect(
#             db='testdb',
#             host='mongodb://localhost',
#             alias='default',
#             mongo_client_class=mongomock.MongoClient
#         )

#     @classmethod
#     def tearDownClass(cls):
#         Driver.objects.delete()
#         disconnect(alias='default')
#         cls.mock_connection.close()
#         super().tearDownClass()

#     def setUp(self):
#         self.valid_driver_data = {
#             'name': 'John Doe',
#             'email': 'john@example.com',
#             'birthYear': '1990-01-01',
#             'password': 'password123',
#             'cpf': '98765432109',
#             'phone': '+55 31 8765-4321',
#             'birthYear':"1990-01-01",
#             'licenseType': 'B',
#             'licenseNumber': '987654',
#             'performance': 5,
#             'isActive': True,
#             'type': 'Motorista'
#         }
#         response = self.client.post(reverse('drivers:create_driver'), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_retrieve_driver_details(self):
#         # Test GET /drivers/<id>/
#         response = self.client.get(reverse('drivers:get_driver', kwargs={'driver_id': str(self.driver.id)}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_driver(self):
#         # Test PUT /drivers/<id>/
#         data = {
#             'name': 'John Doe Updated',
#             'email': 'john.updated@example.com',
#             'password': 'password123',
#             'cpf': '12345678901',
#             'phone': '+55 31 1234-5678',
#             'licenseType': 'A',
#             'licenseNumber': '123456',
#             'performance': 5,
#             'isActive': True,
#             'type': 'Motorista'
#         }
#         response = self.client.put(reverse('drivers:update_driver', kwargs={'driver_id': str(self.driver.id)}), data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.driver.reload()

#     def test_delete_driver(self):
#         # Test DELETE /drivers/<id>/
#         response = self.client.delete(reverse('drivers:delete_driver', kwargs={'driver_id': str(self.driver.id)}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)