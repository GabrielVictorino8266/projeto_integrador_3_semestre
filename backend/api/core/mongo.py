"""
Simple Singleton class that provides a connection to a MongoDB instance.

The `get_client` method returns a MongoClient instance that connects to the
MongoDB instance specified in the `MONGO_URI` environment variable.

The connection is lazy-loaded, meaning that it is only created when the
`get_client` method is first called.
"""
from django.conf import settings
from pymongo import MongoClient

class MongoConnection:
    _client = None

    @classmethod
    def get_client(cls):
        # Check if the client has already been created
        if cls._client is None:
            # Create a new MongoClient instance using the MONGO_URI environment variable
            cls._client = MongoClient(settings.MONGO_URI)

        # Return the MongoClient instance
        return cls._client

    @classmethod
    def get_database(cls):
        return cls.get_client()[settings.MONGO_DB_NAME]