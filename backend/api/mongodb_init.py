import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def initialize_collections():
    """Initialize MongoDB collections with proper indexes"""
    mongo_uri = os.getenv('MONGO_URI')
    mongo_db_name = os.getenv('MONGO_DB_NAME')
    
    if not mongo_uri or not mongo_db_name:
        raise ValueError("MONGO_URI and MONGO_DB_NAME must be set in environment")
    
    try:
        # Verify connection
        client = MongoClient(mongo_uri)
        db = client[mongo_db_name]
        db.command('ping')  # Test connection
        
        # Create collections and indexes
        collections = [
            {
                'name': 'driver',
                'indexes': [
                    {'key': {'name': 1}, 'unique': True},
                    {'key': {'email': 1}, 'unique': True},
                    {'key': {'cpf': 1}, 'unique': True},
                    {'key': {'licenseNumber': 1}, 'unique': True}
                ]
            },
            {
                'name': 'refresh_tokens',
                'indexes': [
                    {'key': {'token': 1}, 'unique': True},
                    {'key': {'user_id': 1}}
                ]
            },
            {
                'name': 'token_blacklist',
                'indexes': [
                    {'key': {'token': 1}, 'unique': True},
                    {'key': {'user_id': 1}}
                ]
            },
            {
                'name': 'users',
                'indexes': [
                    {'key': {'email': 1}, 'unique': True},
                    {'key': {'username': 1}, 'unique': True}
                ]
            },
            {
                'name': 'vehicle',
                'indexes': [
                    {'key': {'plate': 1}, 'unique': True},
                    {'key': {'driver_id': 1}}
                ]
            }
        ]
        
        for collection in collections:
            try:
                db.create_collection(collection['name'])
                for index in collection['indexes']:
                    db[collection['name']].create_index(
                        index['key'],
                        unique=index.get('unique', False)
                    )
            except:
                continue
        
        # Verify collections were created
        existing_collections = db.list_collection_names()
        for collection in collections:
            if collection['name'] not in existing_collections:
                raise ValueError(f"Failed to create collection: {collection['name']}")
        
    except Exception as e:
        raise RuntimeError(f"Failed to initialize MongoDB: {str(e)}")
    finally:
        if 'client' in locals():
            client.close()

if __name__ == "__main__":
    initialize_collections()
