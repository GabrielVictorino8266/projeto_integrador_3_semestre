from django.core.management.base import BaseCommand
from django.conf import settings
from mongodb_migrations.cli import MigrationManager
from mongodb_migrations.config import Configuration
import os
import io
import sys

class Command(BaseCommand):
    help = 'Cria um novo arquivo de migração para o MongoDB'

    def add_arguments(self, parser):
        parser.add_argument(
            'description',
            type=str,
            help='Descrição da migração. Será usada no nome do arquivo.'
        )

    def handle(self, *args, **options):
        mongo_uri = settings.MONGO_URI
        mongo_db_name = settings.MONGO_DB_NAME
        migrations_dir = settings.MIGRATIONS_DIR
        description = options['description']

        self.stdout.write(f'Criando migração do MongoDB: {description}')

        config = Configuration({
            'mongo_url': mongo_uri,
            'mongo_database': mongo_db_name,
            'mongo_migrations_path': migrations_dir,
            'description': description
        })

        # BUG: biblioteca mongodb_migrations não aceita description como parâmetro
        if not config.description:
            config.description = description

        manager = MigrationManager(config=config)

        try:
            captured_output = io.StringIO()
            sys.stdout = captured_output
            manager.create_migration()
            captured_output.seek(0)
            output = captured_output.read()
            self.stdout.write(self.style.SUCCESS(output))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Erro ao criar migração: {e}'))