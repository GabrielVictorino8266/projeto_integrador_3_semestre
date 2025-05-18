from django.core.management.base import BaseCommand
from pymongo import MongoClient
import os
from dotenv import load_dotenv



class Command(BaseCommand):
    help = 'Testa a conexão com MongoDB'

    def clean_environment(self):
        # Remover uma variável específica
        if 'MONGO_URI' in os.environ:
            del os.environ['MONGO_URI']

        # Remover múltiplas variáveis
        for key in ['MONGO_URI', 'MONGO_DB_NAME', 'SECRET_KEY']:
            if key in os.environ:
                del os.environ[key]

        # Imprimir todas as variáveis de ambiente
        print("=== Variáveis de ambiente ===")
        for key, value in os.environ.items():
            print(f"{key} = {value}")
    

    def handle(self, *args, **options):
        try:
            # self.clean_environment()
            load_dotenv()
            
            # Ou imprimir apenas as que você quer
            print(f"MONGO_URI = {os.environ.get('MONGO_URI')}")
            print(f"MONGO_DB_NAME = {os.environ.get('MONGO_DB_NAME')}")
            # Conectar diretamente
            MONGO_URI = os.environ.get('MONGO_URI', 'mongodb+srv://projetointegradorfatecararas:V1VEQNL2Q1PBXLVi@test.jw0sbz1.mongodb.net/')
            MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'projeto_teste')
            
            client = MongoClient(MONGO_URI)
            db = client[MONGO_DB_NAME]
            
            # Testar conexão
            info = client.server_info()
            self.stdout.write(self.style.SUCCESS('✅ Conexão MongoDB OK!'))
            self.stdout.write(f'📊 Banco de dados: {MONGO_DB_NAME}')
            
            collections = db.list_collection_names()
            self.stdout.write(f'📋 Coleções: {", ".join(collections) or "Nenhuma coleção encontrada"}')
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Erro: {e}'))