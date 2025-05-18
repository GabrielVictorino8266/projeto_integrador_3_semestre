#app/services/mongo_service.py
from django.conf import settings

class MongoService:
    @staticmethod
    def get_collection(collection_name: str):
        """
        Returns a mongodb collection by name
        """
        return settings.db[collection_name]

    @staticmethod
    def create_document(collection_name: str, document: dict):
        """
        Creates a document in the collection specified by name
        """
        collection = MongoService.get_collection(collection_name)
        return collection.insert_one(document)

    @staticmethod
    def find_documents(collection_name: str, query=None, projection=None):
        """
        Finds documents in the collection name specified by a query
        """
        collection = MongoService.get_collection(collection_name)
        return collection.find(query or {}, projection or {})

    @staticmethod
    def find_one(collection_name: str, query=None):
        """
        Find a single document in the collection
        """
        collection = MongoService.get_collection(collection_name)
        return collection.find_one(query)
    