from django.core.management.base import BaseCommand
from django.conf import settings
from mongodb_migrations.cli import MigrationManager
from mongodb_migrations.config import Configuration

class Command(BaseCommand):
    help = 'Executa as migrações do MongoDB usando mongodb-migrations.'

    def handle(self, *args, **options):
        mongo_uri = settings.MONGO_URI
        mongo_db_name = settings.MONGO_DB_NAME
        migrations_dir = settings.MIGRATIONS_DIR

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
