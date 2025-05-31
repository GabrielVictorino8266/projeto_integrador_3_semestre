from django.core.management.base import BaseCommand
from django.conf import settings
from mongodb_migrations.cli import MigrationManager
from mongodb_migrations.config import Configuration
import os

class Command(BaseCommand):
    help = 'Executa as migrações do MongoDB usando mongodb-migrations.'

    def handle(self, *args, **options):
        mongo_uri = settings.MONGO_URI
        mongo_db_name = settings.MONGO_DB_NAME

        if not mongo_uri:
            self.stderr.write(self.style.ERROR('MONGO_URI não configurado nas variáveis de ambiente'))
            return

        migrations_dir = os.path.join(settings.BASE_DIR, 'database', 'migrations')

        if not os.path.isdir(migrations_dir):
            self.stderr.write(self.style.ERROR(f'Diretório de migrações não encontrado: {migrations_dir}'))
            return

        self.stdout.write(f'Executando migrações do MongoDB a partir de: {migrations_dir}')

        manager = MigrationManager(
            config=Configuration({
                'mongo_url': mongo_uri,
                'mongo_database': mongo_db_name,
                'mongo_migrations_path': migrations_dir
            })
        )

        try:
            manager.run()
            self.stdout.write(self.style.SUCCESS('Migrações do MongoDB aplicadas com sucesso.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Erro ao executar as migrações: {e}'))
