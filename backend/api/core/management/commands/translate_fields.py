# app_name/management/commands/translate_mongo_fields.py

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from pymongo import MongoClient
import os

class Command(BaseCommand):
    help = 'Translates MongoDB collection fields from Portuguese to English (including incidents)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--collection',
            type=str,
            default='users',
            help='Collection name to translate (default: users)',
        )
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Show what would be changed without making actual changes',
        )
        parser.add_argument(
            '--confirm',
            action='store_true',
            help='Skip confirmation prompt',
        )
        parser.add_argument(
            '--incidents-only',
            action='store_true',
            help='Translate only incident fields (skip document-level fields)',
        )

    def handle(self, *args, **options):
        # Usar as mesmas variáveis do seu .env
        mongo_uri = os.getenv('MONGO_URI')
        if not mongo_uri:
            raise CommandError("MONGO_URI environment variable is required")

        database_name = os.environ.get('MONGO_DB_NAME', 'projeto_teste')
        collection_name = options['collection']
        
        # Mapeamento baseado no seu documento real (campos que ainda não foram traduzidos)
        document_field_mapping = {
            # Removido campos que já estão traduzidos no seu exemplo
            # Apenas campos que ainda estão em português
        }
        
        # Mapeamento para campos dentro dos incidents
        incidents_field_mapping = {
            'data': 'date',
            'tipo': 'type',
            'gravidade': 'severity',
            'peso': 'importance',
            'texto': 'description'
        }

        self.stdout.write(f"Connecting to database: {database_name}")
        self.stdout.write(f"Collection: {collection_name}")
        
        try:
            client = MongoClient(mongo_uri)
            db = client[database_name]
            collection = db[collection_name]
            
            # Verificar se a coleção existe e tem documentos
            doc_count = collection.count_documents({})
            if doc_count == 0:
                self.stdout.write(
                    self.style.WARNING(f"Collection '{collection_name}' is empty or doesn't exist")
                )
                return

            self.stdout.write(f"Found {doc_count} documents to process")
            
            # Verificar quais campos existem na coleção
            sample_doc = collection.find_one()
            
            # Verificar campos do documento principal
            existing_document_fields = []
            if not options['incidents_only']:
                existing_document_fields = [field for field in document_field_mapping.keys() if field in sample_doc]
            
            # Verificar campos dos incidents
            existing_incident_fields = []
            docs_with_incidents = 0
            if sample_doc and 'incidents' in sample_doc and sample_doc['incidents']:
                docs_with_incidents = collection.count_documents({"incidents": {"$exists": True, "$ne": []}})
                if docs_with_incidents > 0:
                    sample_incident = sample_doc['incidents'][0] if isinstance(sample_doc['incidents'], list) else sample_doc['incidents']
                    existing_incident_fields = [field for field in incidents_field_mapping.keys() if field in sample_incident]
            
            if not existing_document_fields and not existing_incident_fields:
                self.stdout.write(
                    self.style.WARNING("No matching fields found to translate")
                )
                self.stdout.write("Available fields in sample document:")
                for key in sample_doc.keys():
                    if key != '_id':
                        self.stdout.write(f"  - {key}")
                        
                if sample_doc.get('incidents') and len(sample_doc['incidents']) > 0:
                    self.stdout.write("Available incident fields:")
                    sample_incident = sample_doc['incidents'][0]
                    for key in sample_incident.keys():
                        self.stdout.write(f"  - incidents.{key}")
                return

            # Mostrar mapeamento de campos que serão traduzidos
            if existing_document_fields:
                self.stdout.write("\nDocument fields to be translated:")
                for old_field in existing_document_fields:
                    new_field = document_field_mapping[old_field]
                    self.stdout.write(f"  {old_field} → {new_field}")
                    
            if existing_incident_fields:
                self.stdout.write(f"\nIncident fields to be translated ({docs_with_incidents} documents with incidents):")
                for old_field in existing_incident_fields:
                    new_field = incidents_field_mapping[old_field]
                    self.stdout.write(f"  incidents.{old_field} → incidents.{new_field}")

            # Dry run
            if options['dry_run']:
                self.stdout.write(
                    self.style.SUCCESS("\nDRY RUN - No changes will be made")
                )
                
                if existing_document_fields:
                    pipeline = self._build_document_pipeline(document_field_mapping, existing_document_fields)
                    sample_result = list(collection.aggregate(pipeline + [{"$limit": 1}]))
                    if sample_result:
                        self.stdout.write("Sample document after translation:")
                        for key, value in sample_result[0].items():
                            if key != '_id' and key != 'incidents':
                                self.stdout.write(f"  {key}: {value}")
                
                if existing_incident_fields:
                    pipeline = self._build_incidents_pipeline(incidents_field_mapping, existing_incident_fields)
                    sample_result = list(collection.aggregate(pipeline + [{"$limit": 1}]))
                    if sample_result and sample_result[0].get('incidents'):
                        self.stdout.write("Sample incident after translation:")
                        incident = sample_result[0]['incidents'][0]
                        for key, value in incident.items():
                            self.stdout.write(f"  incidents.{key}: {value}")
                return

            # Confirmação
            total_operations = len(existing_document_fields) + (1 if existing_incident_fields else 0)
            if not options['confirm']:
                confirm = input(f"\nThis will perform {total_operations} translation operations on {doc_count} documents. Continue? [y/N]: ")
                if confirm.lower() not in ['y', 'yes']:
                    self.stdout.write("Operation cancelled")
                    return

            # Executar traduções
            self._execute_translations(client, collection, document_field_mapping, existing_document_fields, 
                                     incidents_field_mapping, existing_incident_fields)
            
        except Exception as e:
            raise CommandError(f"Error during translation: {str(e)}")
        finally:
            if 'client' in locals():
                client.close()

    def _build_document_pipeline(self, field_mapping, existing_fields):
        """Constrói pipeline de agregação para renomear campos do documento"""
        add_fields_stage = {}
        for old_field in existing_fields:
            new_field = field_mapping[old_field]
            add_fields_stage[new_field] = f"${old_field}"
        
        unset_stage = existing_fields
        
        return [
            {"$addFields": add_fields_stage},
            {"$unset": unset_stage}
        ]
    
    def _build_incidents_pipeline(self, incidents_mapping, existing_incident_fields):
        """Constrói pipeline de agregação para renomear campos dos incidents"""
        return [
            {
                "$addFields": {
                    "incidents": {
                        "$map": {
                            "input": "$incidents",
                            "as": "incident",
                            "in": {
                                # Primeiro, manter todos os campos existentes
                                "$mergeObjects": [
                                    "$$incident",
                                    # Depois, adicionar campos traduzidos
                                    {
                                        **{
                                            incidents_mapping[old_field]: f"$$incident.{old_field}"
                                            for old_field in existing_incident_fields
                                        }
                                    }
                                ]
                            }
                        }
                    }
                }
            },
            {
                # Remover campos antigos em português dos incidents
                "$addFields": {
                    "incidents": {
                        "$map": {
                            "input": "$incidents",
                            "as": "incident",
                            "in": {
                                "$arrayToObject": {
                                    "$filter": {
                                        "input": {"$objectToArray": "$$incident"},
                                        "cond": {
                                            "$not": {
                                                "$in": ["$$this.k", existing_incident_fields]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        ]

    def _execute_translations(self, client, collection, document_field_mapping, existing_document_fields,
                            incidents_field_mapping, existing_incident_fields):
        """Executa as traduções dos campos com transação"""
        
        try:
            # Usar transação para garantir atomicidade
            with client.start_session() as session:
                with session.start_transaction():
                    
                    # 1. Traduzir campos do documento principal
                    if existing_document_fields:
                        self.stdout.write("Translating document-level fields...")
                        pipeline = self._build_document_pipeline(document_field_mapping, existing_document_fields)
                        
                        # Obter todos os documentos traduzidos
                        updated_docs = list(collection.aggregate(pipeline, session=session))
                        
                        if updated_docs:
                            # Remover documentos antigos
                            delete_result = collection.delete_many({}, session=session)
                            self.stdout.write(f"Deleted {delete_result.deleted_count} old documents")
                            
                            # Inserir documentos traduzidos
                            insert_result = collection.insert_many(updated_docs, session=session)
                            self.stdout.write(f"Inserted {len(insert_result.inserted_ids)} documents with translated fields")
                    
                    # 2. Traduzir campos dos incidents
                    if existing_incident_fields:
                        self.stdout.write("Translating incident fields...")
                        pipeline = self._build_incidents_pipeline(incidents_field_mapping, existing_incident_fields)
                        
                        # Aplicar transformação usando update com pipeline
                        result = collection.update_many(
                            {"incidents": {"$exists": True, "$ne": []}},
                            pipeline,
                            session=session
                        )
                        
                        self.stdout.write(f"Updated incident fields in {result.modified_count} documents")
                    
                    # Resultado final
                    total_translated = len(existing_document_fields) + len(existing_incident_fields)
                    self.stdout.write(
                        self.style.SUCCESS(f"\n✅ Successfully translated {total_translated} field types!")
                    )
                    
                    if existing_document_fields:
                        self.stdout.write(f"   - Document fields: {', '.join(existing_document_fields)}")
                    if existing_incident_fields:
                        self.stdout.write(f"   - Incident fields: {', '.join(existing_incident_fields)}")
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ Error during field translation: {str(e)}")
            )
            raise