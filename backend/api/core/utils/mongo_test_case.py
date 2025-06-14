from mongomock import MongoClient
from rest_framework.test import APITestCase
from mongoengine import connect, disconnect

class MongoTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Conecta a uma instância MongoDB em memória usando mongomock
        disconnect(alias='default')
        connect(mongo_client_class=MongoClient)

    @classmethod
    def tearDownClass(cls):
        # Desconecta da instância MongoDB mockada
        disconnect(alias='testdb')
        super().tearDownClass()
