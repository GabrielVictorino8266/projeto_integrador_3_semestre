import os
from dotenv import load_dotenv
from pymongo import MongoClient
import unittest

load_dotenv()

class TestMongoDBConnection(unittest.TestCase):
    def setUp(self):
        self.mongo_uri = os.getenv('MONGO_URI')
        self.mongo_db_name = os.getenv('MONGO_DB_NAME')
        self.client = None
        self.db = None

    def test_connection(self):
        """Test MongoDB connection"""
        if not self.mongo_uri or not self.mongo_db_name:
            self.fail("MONGO_URI or MONGO_DB_NAME not set in environment")

        try:
            self.client = MongoClient(self.mongo_uri)
            self.db = self.client[self.mongo_db_name]
            # Test connection by running a simple command
            self.db.command('ping')
        except Exception as e:
            self.fail(f"MongoDB connection failed: {str(e)}")

    def test_collections_exist(self):
        """Test if required collections exist"""
        required_collections = [
            'driver',
            'refresh_tokens',
            'token_blacklist',
            'users',
            'vehicle'
        ]

        if not self.db:
            self.fail("Database connection not established")

        existing_collections = self.db.list_collection_names()
        
        for collection in required_collections:
            self.assertIn(collection, existing_collections, 
                         f"Collection {collection} does not exist")

    def tearDown(self):
        if self.client:
            self.client.close()

if __name__ == '__main__':
    unittest.main()
