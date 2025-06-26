# core/management/commands/export_collection.py
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from pymongo import MongoClient
import json
import csv
import os
from datetime import datetime
from bson import ObjectId
from bson.json_util import dumps

class Command(BaseCommand):
    help = 'Exporta uma collection do MongoDB para diferentes formatos (JSON, CSV)'

    def add_arguments(self, parser):
        # Argumentos obrigatórios
        parser.add_argument(
            'collection_name',
            type=str,
            help='Nome da collection a ser exportada'
        )
        
        # Argumentos opcionais
        parser.add_argument(
            '--format',
            choices=['json', 'csv'],
            default='json',
            help='Formato de exportação (padrão: json)'
        )
        
        parser.add_argument(
            '--output',
            type=str,
            help='Caminho do arquivo de saída (se não especificado, usa nome automático)'
        )
        
        parser.add_argument(
            '--filter',
            type=str,
            help='Filtro MongoDB em formato JSON (ex: {"tipo": "admin"})'
        )
        
        parser.add_argument(
            '--fields',
            type=str,
            help='Campos a serem incluídos, separados por vírgula (ex: cpf,tipo,ativo)'
        )
        
        parser.add_argument(
            '--limit',
            type=int,
            help='Limitar número de documentos exportados'
        )
        
        parser.add_argument(
            '--pretty',
            action='store_true',
            help='Formatar JSON de forma legível (apenas para JSON)'
        )
        
        parser.add_argument(
            '--exclude-id',
            action='store_true',
            help='Excluir campo _id da exportação'
        )

    def handle(self, *args, **options):
        collection_name = options['collection_name']
        
        # Conectar ao MongoDB
        try:
            MONGO_URI = os.environ.get('MONGO_URI')
            MONGO_DB_NAME = os.environ.get('MONGO_DB_NAME', 'projeto_teste')
            
            if not MONGO_URI:
                raise CommandError('MONGO_URI não configurada nas variáveis de ambiente')
            
            mongo_client = MongoClient(MONGO_URI)
            mongodb = mongo_client[MONGO_DB_NAME]
            collection = mongodb[collection_name]
            
            self.stdout.write(
                self.style.SUCCESS(f'✓ Conectado ao MongoDB: {MONGO_DB_NAME}')
            )
            
        except Exception as e:
            raise CommandError(f'Erro ao conectar ao MongoDB: {e}')

        # Verificar se a collection existe
        if collection_name not in mongodb.list_collection_names():
            raise CommandError(f'Collection "{collection_name}" não encontrada')

        # Preparar filtro
        mongo_filter = {}
        if options['filter']:
            try:
                mongo_filter = json.loads(options['filter'])
                self.stdout.write(f'📋 Filtro aplicado: {mongo_filter}')
            except json.JSONDecodeError:
                raise CommandError('Filtro deve ser um JSON válido')

        # Preparar projeção de campos
        projection = None
        if options['fields']:
            fields = [field.strip() for field in options['fields'].split(',')]
            projection = {field: 1 for field in fields}
            
            # Incluir _id apenas se não foi excluído explicitamente
            if not options['exclude_id'] and '_id' not in fields:
                projection['_id'] = 1
            elif options['exclude_id']:
                projection['_id'] = 0
                
            self.stdout.write(f'📑 Campos selecionados: {", ".join(fields)}')
        elif options['exclude_id']:
            projection = {'_id': 0}

        # Buscar documentos
        try:
            cursor = collection.find(mongo_filter, projection)
            
            if options['limit']:
                cursor = cursor.limit(options['limit'])
                self.stdout.write(f'📊 Limitado a {options["limit"]} documentos')
            
            documents = list(cursor)
            
            if not documents:
                self.stdout.write(
                    self.style.WARNING(f'⚠ Nenhum documento encontrado na collection "{collection_name}"')
                )
                return
                
            self.stdout.write(f'📦 Encontrados {len(documents)} documentos')
            
        except Exception as e:
            raise CommandError(f'Erro ao buscar documentos: {e}')

        # Gerar nome do arquivo se não especificado
        if not options['output']:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            extension = options['format']
            options['output'] = f'{collection_name}_export_{timestamp}.{extension}'

        # Exportar conforme o formato
        try:
            if options['format'] == 'json':
                self._export_json(documents, options)
            elif options['format'] == 'csv':
                self._export_csv(documents, options)
                
        except Exception as e:
            raise CommandError(f'Erro durante exportação: {e}')
        finally:
            mongo_client.close()

    def _export_json(self, documents, options):
        """Exporta documentos para formato JSON"""
        output_file = options['output']
        
        with open(output_file, 'w', encoding='utf-8') as f:
            if options['pretty']:
                # Usar bson.json_util para lidar com ObjectId e outros tipos BSON
                json_str = dumps(documents, indent=2, ensure_ascii=False)
                f.write(json_str)
            else:
                json_str = dumps(documents, ensure_ascii=False)
                f.write(json_str)
        
        file_size = os.path.getsize(output_file)
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Exportação JSON concluída!\n'
                f'   📁 Arquivo: {output_file}\n'
                f'   📊 Tamanho: {file_size:,} bytes\n'
                f'   📦 Documentos: {len(documents)}'
            )
        )

    def _export_csv(self, documents, options):
        """Exporta documentos para formato CSV"""
        if not documents:
            raise CommandError('Nenhum documento para exportar')
        
        output_file = options['output']
        
        # Obter todos os campos únicos dos documentos
        all_fields = set()
        for doc in documents:
            all_fields.update(self._flatten_dict(doc).keys())
        
        all_fields = sorted(list(all_fields))
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=all_fields)
            writer.writeheader()
            
            for doc in documents:
                flattened = self._flatten_dict(doc)
                # Converter ObjectId para string
                for key, value in flattened.items():
                    if isinstance(value, ObjectId):
                        flattened[key] = str(value)
                
                writer.writerow(flattened)
        
        file_size = os.path.getsize(output_file)
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Exportação CSV concluída!\n'
                f'   📁 Arquivo: {output_file}\n'
                f'   📊 Tamanho: {file_size:,} bytes\n'
                f'   📦 Documentos: {len(documents)}\n'
                f'   📑 Colunas: {len(all_fields)}'
            )
        )

    def _flatten_dict(self, d, parent_key='', sep='_'):
        """
        Achata dicionários aninhados para uso em CSV
        Ex: {'user': {'name': 'João'}} -> {'user_name': 'João'}
        """
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key, sep=sep).items())
            elif isinstance(v, list):
                # Para listas, converter para string
                items.append((new_key, str(v)))
            else:
                items.append((new_key, v))
        
        return dict(items)