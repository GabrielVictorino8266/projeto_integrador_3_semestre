from mongodb_migrations.base import BaseMigration
from pymongo import MongoClient
import os
from datetime import datetime

class Migration(BaseMigration):
    def upgrade(self):
        mongo_uri = os.getenv('MONGO_URI')
        db_name = os.getenv('MONGO_DB_NAME')
        
        if not mongo_uri or not db_name:
            raise ValueError("MONGO_URI e MONGO_DB_NAME devem estar configurados")
            
        client = MongoClient(mongo_uri)
        db = client[db_name]
        
        if 'users' not in db.list_collection_names():
            print("Criando coleção users...")
            db.create_collection('users')
            db.users.create_index([('email', 1)], unique=False, sparse=True)
            db.users.create_index([('cpf', 1)], unique=True)
            print("Coleção users criada com sucesso")
        
        import hashlib
        
        def get_hash_password(password):
            return hashlib.sha256(password.encode()).hexdigest()
        
        drivers = [
            {
                "cpf": "11111111112",
                "name": "Juliano Aparecido",
                "birthYear": "1980-01-01",
                "phone": "1111111111",
                "licenseType": "C",
                "licenseNumber": "111111",
                "performance": 1,
                "incidents": [],
                "password": get_hash_password(f"12{1980}")
            },
            {
                "cpf": "22222222223",
                "name": "Rian Scavazza",
                "birthYear": "1985-02-02",
                "phone": "2222222222",
                "licenseType": "C",
                "licenseNumber": "222222",
                "performance": 1,
                "incidents": [],
                "password": get_hash_password(f"23{1985}")
            },
            {
                "cpf": "33333333334",
                "name": "Gabriel Victorino",
                "birthYear": "1990-03-03",
                "phone": "3333333333",
                "licenseType": "C",
                "licenseNumber": "333333",
                "performance": 1,
                "incidents": [],
                "password": get_hash_password(f"34{1990}")
            },
            {
                "cpf": "44444444445",
                "name": "Bruno Alexander",
                "birthYear": "1995-04-04",
                "phone": "4444444444",
                "licenseType": "C",
                "licenseNumber": "444444",
                "performance": 1,
                "incidents": [],
                "password": get_hash_password(f"45{1995}")
            },
            {
                "cpf": "55555555556",
                "name": "Gustavo Francisco",
                "birthYear": "2000-05-05",
                "phone": "5555555555",
                "licenseType": "C",
                "licenseNumber": "555555",
                "performance": 1,
                "incidents": [],
                "password": get_hash_password(f"56{2000}")
            },
            {
                "cpf": "66666666667",
                "name": "Raphel Reis",
                "birthYear": "2000-05-05",
                "phone": "6666666666",
                "licenseType": "C",
                "licenseNumber": "666666",
                "performance": 1,
                "incidents": [],
                "password": get_hash_password(f"67{2000}")
            }
        ]
        
        result = db.users.insert_many(drivers)
        print(f"Inseridos {len(result.inserted_ids)} drivers na coleção users")
        
        if len(result.inserted_ids) != len(drivers):
            raise ValueError("Falha ao inserir todos os drivers na coleção users")

    def downgrade(self):
        mongo_uri = os.getenv('MONGO_URI')
        db_name = os.getenv('MONGO_DB_NAME')
        
        if not mongo_uri or not db_name:
            raise ValueError("MONGO_URI e MONGO_DB_NAME devem estar configurados")
            
        client = MongoClient(mongo_uri)
        db = client[db_name]
        
        db.users.delete_many({
            "cpf": {
                "$in": [
                    "11111111112",
                    "22222222223",
                    "33333333334",
                    "44444444445",
                    "55555555556",
                    "66666666667"
                ]
            }
        })
        print("Drivers removidos com sucesso")
        db.drop_collection('users')
        print("Coleção users removida com sucesso")

