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
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"12{1980}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "22222222223",
                "name": "Rian Scavazza",
                "birthYear": "1985-02-02",
                "phone": "2222222222",
                "licenseType": "C",
                "licenseNumber": "222222",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"23{1985}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "33333333334",
                "name": "Gabriel Victorino",
                "birthYear": "1990-03-03",
                "phone": "3333333333",
                "licenseType": "C",
                "licenseNumber": "333333",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"34{1990}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "44444444445",
                "name": "Bruno Alexander",
                "birthYear": "1995-04-04",
                "phone": "4444444444",
                "licenseType": "C",
                "licenseNumber": "444444",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"45{1995}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "55555555556",
                "name": "Gustavo Francisco",
                "birthYear": "2000-05-05",
                "phone": "5555555555",
                "licenseType": "C",
                "licenseNumber": "555555",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"56{2000}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "66666666667",
                "name": "Raphael Reis",
                "birthYear": "2000-05-05",
                "phone": "6666666666",
                "licenseType": "C",
                "licenseNumber": "666666",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"67{2000}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
                        {
                "cpf": "77777777778",
                "name": "Lucas Mendes",
                "birthYear": "1988-07-15",
                "phone": "7777777777",
                "licenseType": "D",
                "licenseNumber": "777777",
                "performance": 9,
                "incidents": [],
                "password": get_hash_password(f"78{1988}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "88888888889",
                "name": "Pedro Alves",
                "birthYear": "1992-09-22",
                "phone": "8888888888",
                "licenseType": "E",
                "licenseNumber": "888888",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"89{1992}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "99999999990",
                "name": "Marcos Silva",
                "birthYear": "1987-11-30",
                "phone": "9999999999",
                "licenseType": "D",
                "licenseNumber": "999999",
                "performance": 8,
                "incidents": [],
                "password": get_hash_password(f"90{1987}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "12345678901",
                "name": "Carlos Eduardo",
                "birthYear": "1991-04-18",
                "phone": "1234567890",
                "licenseType": "C",
                "licenseNumber": "112233",
                "performance": 9,
                "incidents": [],
                "password": get_hash_password(f"01{1991}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "23456789012",
                "name": "Fernando Costa",
                "birthYear": "1993-06-25",
                "phone": "2345678901",
                "licenseType": "D",
                "licenseNumber": "223344",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"12{1993}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "34567890123",
                "name": "Ricardo Oliveira",
                "birthYear": "1989-08-12",
                "phone": "3456789012",
                "licenseType": "E",
                "licenseNumber": "334455",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"23{1989}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "45678901234",
                "name": "André Santos",
                "birthYear": "1994-10-05",
                "phone": "4567890123",
                "licenseType": "D",
                "licenseNumber": "445566",
                "performance": 9,
                "incidents": [],
                "password": get_hash_password(f"34{1994}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "56789012345",
                "name": "Thiago Pereira",
                "birthYear": "1990-12-15",
                "phone": "5678901234",
                "licenseType": "C",
                "licenseNumber": "556677",
                "performance": 8,
                "incidents": [],
                "password": get_hash_password(f"45{1990}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "67890123456",
                "name": "Roberto Almeida",
                "birthYear": "1986-03-22",
                "phone": "6789012345",
                "licenseType": "D",
                "licenseNumber": "667788",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"56{1986}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "78901234567",
                "name": "Leonardo Martins",
                "birthYear": "1995-05-30",
                "phone": "7890123456",
                "licenseType": "E",
                "licenseNumber": "778899",
                "performance": 9,
                "incidents": [],
                "password": get_hash_password(f"67{1995}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
                        {
                "cpf": "89012345678",
                "name": "Diego Ramos",
                "birthYear": "1993-07-14",
                "phone": "8901234567",
                "licenseType": "D",
                "licenseNumber": "889900",
                "performance": 9,
                "incidents": [],
                "password": get_hash_password(f"78{1993}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "90123456789",
                "name": "Eduardo Lima",
                "birthYear": "1988-09-22",
                "phone": "9012345678",
                "licenseType": "E",
                "licenseNumber": "990011",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"89{1988}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "11223344556",
                "name": "Felipe Castro",
                "birthYear": "1991-11-30",
                "phone": "1122334455",
                "licenseType": "D",
                "licenseNumber": "112244",
                "performance": 8,
                "incidents": [],
                "password": get_hash_password(f"56{1991}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "22334455667",
                "name": "Guilherme Rocha",
                "birthYear": "1994-04-18",
                "phone": "2233445566",
                "licenseType": "C",
                "licenseNumber": "223355",
                "performance": 9,
                "incidents": [],
                "password": get_hash_password(f"67{1994}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "33445566778",
                "name": "Henrique Nunes",
                "birthYear": "1989-06-25",
                "phone": "3344556677",
                "licenseType": "D",
                "licenseNumber": "334466",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"78{1989}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "44556677889",
                "name": "Igor Santos",
                "birthYear": "1992-08-12",
                "phone": "4455667788",
                "licenseType": "E",
                "licenseNumber": "445577",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"89{1992}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "55667788990",
                "name": "João Vitor",
                "birthYear": "1995-10-05",
                "phone": "5566778899",
                "licenseType": "D",
                "licenseNumber": "556688",
                "performance": 9,
                "incidents": [],
                "password": get_hash_password(f"90{1995}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "66778899001",
                "name": "Kaique Oliveira",
                "birthYear": "1990-12-15",
                "phone": "6677889900",
                "licenseType": "C",
                "licenseNumber": "667799",
                "performance": 8,
                "incidents": [],
                "password": get_hash_password(f"01{1990}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "77889900112",
                "name": "Leandro Costa",
                "birthYear": "1987-03-22",
                "phone": "7788990011",
                "licenseType": "D",
                "licenseNumber": "778800",
                "performance": 10,
                "incidents": [],
                "password": get_hash_password(f"12{1987}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
            },
            {
                "cpf": "88990011223",
                "name": "Matheus Henrique",
                "birthYear": "1993-05-30",
                "phone": "8899001122",
                "licenseType": "E",
                "licenseNumber": "889911",
                "performance": 9,
                "incidents": [],
                "password": get_hash_password(f"23{1993}"),
                "type": "Motorista",
                "isActive": True,
                "deleted": False,
                "createdAt": datetime.now(),
                "updatedAt": datetime.now()
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
                    "66666666667",
                    "77777777778",
                    "88888888889",
                    "99999999990",
                    "12345678901",
                    "23456789012",
                    "34567890123",
                    "45678901234",
                    "56789012345",
                    "67890123456",
                    "78901234567",
                    "89012345678",
                    "90123456789",
                    "11223344556",
                    "22334455667",
                    "33445566778",
                    "44556677889",
                    "55667788990",
                    "66778899001",
                    "77889900112",
                    "88990011223"
                ]
            }
        })
        print("Drivers removidos com sucesso")
        db.drop_collection('users')
        print("Coleção users removida com sucesso")

