import os
from pymongo import MongoClient
from pymongo.errors import OperationFailure, ConnectionFailure
from dotenv import load_dotenv

def test_mongodb_connection():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()
    
    # Obtém as credenciais do ambiente
    mongo_uri = os.getenv('MONGO_URI')
    db_name = os.getenv('MONGO_DB_NAME', 'Test')
    username, password = mongo_uri.split('@')[0].split('/')[-1].split(':')
    
    if not mongo_uri:
        print("ERRO: MONGO_URI não encontrada nas variáveis de ambiente.")
        return
    
    print(f"Conectando ao MongoDB: {mongo_uri}")
    print(f"Banco de dados: {db_name}")
    print(f"Usuário: {username}")
    print(f"Senha: {password}")
    print("-" * 50)
    
    try:
        # Tenta conectar ao MongoDB
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        
        # Testa a conexão
        print("Testando conexão com o servidor...")
        client.server_info()  # Isso irá falhar se não conseguir se conectar
        print("✅ Conexão com o servidor bem-sucedida!")
        
        # Seleciona o banco de dados
        db = client[db_name]
        
        # 1. Testa listagem de coleções
        print("\n1. Listando coleções...")
        collections = db.list_collection_names()
        print(f"Coleções encontradas: {collections}")
        
        # 2. Tenta criar uma coleção de teste
        test_collection = "test_permissions"
        print(f"\n2. Testando criação da coleção '{test_collection}'...")
        if test_collection not in collections:
            db.create_collection(test_collection)
            print(f"✅ Coleção '{test_collection}' criada com sucesso!")
        else:
            print(f"ℹ️  A coleção '{test_collection}' já existe.")
        
        # 3. Testa operações CRUD básicas
        print(f"\n3. Testando operações CRUD na coleção '{test_collection}'...")
        collection = db[test_collection]
        
        # Inserir
        test_doc = {"test": "test_value", "timestamp": "2025-07-06T13:45:00Z"}
        result = collection.insert_one(test_doc)
        print(f"✅ Documento inserido com ID: {result.inserted_id}")
        
        # Ler
        found = collection.find_one({"_id": result.inserted_id})
        print(f"✅ Documento encontrado: {found is not None}")
        
        # Atualizar
        update_result = collection.update_one(
            {"_id": result.inserted_id},
            {"$set": {"status": "updated"}}
        )
        print(f"✅ Documento atualizado: {update_result.modified_count} modificação(ões)")
        
        # Deletar
        delete_result = collection.delete_one({"_id": result.inserted_id})
        print(f"✅ Documento deletado: {delete_result.deleted_count} documento(s) removido(s)")
        
        # 4. Testa a coleção de migrações
        print("\n4. Testando acesso à coleção 'database_migrations'...")
        try:
            migrations = db.database_migrations
            
            # Tenta inserir um documento de teste
            test_migration = {
                "name": "test_migration",
                "applied_at": "2025-07-06T13:45:00Z"
            }
            result = migrations.insert_one(test_migration)
            print("✅ Documento inserido em 'database_migrations'")
            
            # Tenta encontrar o documento
            found = migrations.find_one({"_id": result.inserted_id})
            print("✅ Documento encontrado em 'database_migrations'")
            
            # Remove o documento de teste
            migrations.delete_one({"_id": result.inserted_id})
            print("✅ Documento removido de 'database_migrations'")
            
        except OperationFailure as e:
            print(f"❌ Erro ao acessar 'database_migrations': {e.details}")
            print("\n⚠️  Verifique se o usuário tem as seguintes permissões no MongoDB Atlas:")
            print("   - readWrite no banco de dados")
            print("   - dbAdmin no banco de dados")
            print("   - readWrite no banco de dados admin")
        
    except ConnectionFailure as e:
        print(f"❌ Falha na conexão com o MongoDB: {e}")
        print("Verifique se o URI está correto e se o servidor está acessível.")
    except OperationFailure as e:
        print(f"❌ Erro de operação no MongoDB: {e.details}")
        print("\n⚠️  Possíveis causas:")
        print("1. Credenciais incorretas")
        print("2. IP não autorizado na lista de permissões do MongoDB Atlas")
        print("3. Permissões insuficientes para o usuário")
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
    finally:
        # Limpeza: remove a coleção de teste
        if 'client' in locals():
            try:
                client[db_name][test_collection].drop()
            except:
                pass
            client.close()

if __name__ == "__main__":
    test_mongodb_connection()
