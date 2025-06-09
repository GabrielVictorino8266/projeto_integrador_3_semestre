# management/commands/add_user_types.py
from django.core.management.base import BaseCommand
from pymongo import MongoClient
from django.conf import settings
import logging

class Command(BaseCommand):
    help = 'Add type field to user documents in MongoDB'

    def add_arguments(self, parser):
        parser.add_argument(
            '--type',
            type=str,
            choices=['Motorista', 'Administrador'],
            required=True,
            help='Type to assign to users (Motorista or Administrador)'
        )
        parser.add_argument(
            '--filter-field',
            type=str,
            help='Field to filter users (optional). Example: email, cpf, name'
        )
        parser.add_argument(
            '--filter-value',
            type=str,
            help='Value to filter users by (required if filter-field is provided)'
        )
        parser.add_argument(
            '--all',
            action='store_true',
            help='Apply to all users without filter'
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be updated without making changes'
        )

    def handle(self, *args, **options):
        # MongoDB connection
        try:
            # Adjust this connection string based on your Django settings
            client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
            db = client[settings.DATABASES['default']['NAME']]
            users_collection = db['users']
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to connect to MongoDB: {e}')
            )
            return

        # Build query filter
        query_filter = {}
        
        if options['filter_field'] and options['filter_value']:
            query_filter[options['filter_field']] = options['filter_value']
        elif not options['all']:
            self.stdout.write(
                self.style.ERROR(
                    'You must either provide --filter-field and --filter-value, or use --all'
                )
            )
            return

        # Find matching documents
        try:
            matching_users = list(users_collection.find(query_filter))
            
            if not matching_users:
                self.stdout.write(
                    self.style.WARNING('No users found matching the criteria')
                )
                return

            self.stdout.write(
                self.style.SUCCESS(
                    f'Found {len(matching_users)} user(s) matching the criteria'
                )
            )

            # Show what will be updated
            if options['dry_run']:
                self.stdout.write(self.style.WARNING('DRY RUN MODE - No changes will be made'))
                for user in matching_users:
                    self.stdout.write(f"Would update user: {user.get('name', 'N/A')} - {user.get('email', 'N/A')}")
                return

            # Update documents
            update_result = users_collection.update_many(
                query_filter,
                {'$set': {'type': options['type']}}
            )

            self.stdout.write(
                self.style.SUCCESS(
                    f'Successfully updated {update_result.modified_count} user(s) with type: {options["type"]}'
                )
            )

            # Show updated users
            updated_users = users_collection.find(query_filter)
            for user in updated_users:
                self.stdout.write(
                    f"Updated: {user.get('name', 'N/A')} - {user.get('email', 'N/A')} - Type: {user.get('type', 'N/A')}"
                )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error updating users: {e}')
            )
        finally:
            client.close()


# Alternative version if you're using djongo or mongoengine
# management/commands/add_user_types_mongoengine.py
"""
If you're using MongoEngine instead of PyMongo directly:

from django.core.management.base import BaseCommand
from your_app.models import User  # Replace with your actual User model

class Command(BaseCommand):
    help = 'Add type field to user documents'

    def add_arguments(self, parser):
        parser.add_argument(
            '--type',
            type=str,
            choices=['Motorista', 'Administrador'],
            required=True,
            help='Type to assign to users'
        )
        parser.add_argument(
            '--email',
            type=str,
            help='Filter by email'
        )
        parser.add_argument(
            '--cpf',
            type=str,
            help='Filter by CPF'
        )
        parser.add_argument(
            '--all',
            action='store_true',
            help='Apply to all users'
        )

    def handle(self, *args, **options):
        query = {}
        
        if options['email']:
            query['email'] = options['email']
        elif options['cpf']:
            query['cpf'] = options['cpf']
        elif not options['all']:
            self.stdout.write(
                self.style.ERROR(
                    'You must provide --email, --cpf, or --all'
                )
            )
            return

        users = User.objects.filter(**query)
        
        if not users:
            self.stdout.write(
                self.style.WARNING('No users found')
            )
            return

        updated_count = users.update(type=options['type'])
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Updated {updated_count} user(s) with type: {options["type"]}'
            )
        )
"""