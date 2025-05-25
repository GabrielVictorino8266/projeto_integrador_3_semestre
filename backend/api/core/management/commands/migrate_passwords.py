from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from passlib.context import CryptContext
from pymongo import MongoClient
import os

class Command(BaseCommand):
    help = 'Migra senhas em texto puro para hash bcrypt no MongoDB'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Executa sem fazer alterações, apenas mostra o que seria feito',
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Força a execução sem confirmação',
        )

    def handle(self, *args, **options):
        # Configurar conexão MongoDB
        try:
            # Usar as mesmas configurações do settings
            MONGO_URI = os.environ.get('MONGO_URI')
            MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'projeto_teste')
            
            if not MONGO_URI:
                raise CommandError('MONGO_URI não configurada nas variáveis de ambiente')
            
            # Conexão MongoDB
            mongo_client = MongoClient(MONGO_URI)
            mongodb = mongo_client[MONGO_DB_NAME]
            users_collection = mongodb['users']
            
            self.stdout.write(
                self.style.SUCCESS(f'✓ Conectado ao MongoDB: {MONGO_DB_NAME}')
            )
            
        except Exception as e:
            raise CommandError(f'Erro ao conectar ao MongoDB: {e}')

        # Configurar Passlib
        pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        # Buscar usuários com senhas
        try:
            users = list(users_collection.find({"password": {"$exists": True}}))
            
            if not users:
                self.stdout.write(
                    self.style.WARNING('Nenhum usuário encontrado com campo "password"')
                )
                return
                
            self.stdout.write(f'Encontrados {len(users)} usuários')
            
        except Exception as e:
            raise CommandError(f'Erro ao buscar usuários: {e}')

        # Analisar quantos precisam de migração
        users_to_migrate = []
        users_already_hashed = []
        
        for user in users:
            plain_password = user.get('password', '')
            
            if isinstance(plain_password, str) and not plain_password.startswith('$2'):
                users_to_migrate.append(user)
            else:
                users_already_hashed.append(user)

        # Mostrar estatísticas
        self.stdout.write(f'📊 Estatísticas:')
        self.stdout.write(f'   • Usuários com senha já em hash: {len(users_already_hashed)}')
        self.stdout.write(f'   • Usuários que precisam migração: {len(users_to_migrate)}')

        if not users_to_migrate:
            self.stdout.write(
                self.style.SUCCESS('✓ Todas as senhas já estão em formato hash!')
            )
            return

        # Mostrar usuários que serão migrados
        if options['dry_run']:
            self.stdout.write(
                self.style.WARNING('\n🔍 MODO DRY-RUN - Nenhuma alteração será feita')
            )
        
        self.stdout.write('\n📋 Usuários que serão migrados:')
        for user in users_to_migrate:
            cpf = user.get('cpf', 'N/A')
            current_password = user.get('password', '')
            self.stdout.write(f'   • CPF: {cpf} (senha atual: "{current_password}")')

        # Confirmação
        if not options['force'] and not options['dry_run']:
            confirm = input('\n❓ Deseja continuar com a migração? (y/N): ')
            if confirm.lower() not in ['y', 'yes', 's', 'sim']:
                self.stdout.write(
                    self.style.WARNING('Migração cancelada pelo usuário')
                )
                return

        # Executar migração
        if not options['dry_run']:
            self.stdout.write('\n🔄 Iniciando migração...')
            
            success_count = 0
            error_count = 0
            
            for user in users_to_migrate:
                try:
                    plain_password = user.get('password')
                    cpf = user.get('cpf', 'N/A')
                    
                    # Gerar hash
                    hashed_password = pwd_context.hash(plain_password)
                    
                    # Atualizar no banco
                    result = users_collection.update_one(
                        {"_id": user["_id"]},
                        {"$set": {"password": hashed_password}}
                    )
                    
                    if result.modified_count > 0:
                        self.stdout.write(f'   ✓ CPF {cpf}: senha migrada com sucesso')
                        success_count += 1
                    else:
                        self.stdout.write(f'   ⚠ CPF {cpf}: nenhuma alteração feita')
                        
                except Exception as e:
                    self.stdout.write(f'   ❌ CPF {cpf}: erro - {e}')
                    error_count += 1

            # Resultado final
            self.stdout.write(f'\n📈 Resultado da migração:')
            self.stdout.write(f'   • Sucessos: {success_count}')
            self.stdout.write(f'   • Erros: {error_count}')
            
            if error_count == 0:
                self.stdout.write(
                    self.style.SUCCESS('🎉 Migração concluída com sucesso!')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'⚠ Migração concluída com {error_count} erros')
                )
        else:
            self.stdout.write(
                self.style.SUCCESS('\n✓ Dry-run concluído - use --force para executar')
            )

        # Fechar conexão
        mongo_client.close()