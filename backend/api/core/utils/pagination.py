import math
from typing import Dict, List, Any, Optional
from mongoengine import Document, QuerySet


class Paginator:
    """
    Utilitário de paginação para documentos MongoEngine que imita o formato de paginação do Laravel.
    """
    
    def __init__(self, queryset: QuerySet, per_page: int = 15, base_url: str = "http://localhost", serializer_class=None):
        """
        Inicializa o paginador.
        
        Args:
            queryset: QuerySet do MongoEngine para paginar
            per_page: Número de itens por página (padrão: 15)
            base_url: URL base para links de paginação (padrão: "http://localhost")
        """
        self.queryset = queryset
        self.per_page = per_page
        self.base_url = base_url.rstrip('/')
        self.total = queryset.count()
        self.serializer_class = serializer_class
    
    def paginate(self, page: Optional[int] = 1) -> Dict[str, Any]:
        """
        Pagina o queryset e retorna dados de paginação no estilo Laravel.
        
        Args:
            page: Número da página atual (baseado em 1)
            
        Returns:
            Dicionário contendo dados de paginação e resultados
        """

        # Se a página for None, exibe todos os resultados
        per_page = self.per_page if page else self.total
        last_page = 1 if self.total == 0 else max(1, math.ceil(self.total / per_page))

        # Garante que a página está dentro dos limites válidos
        current_page = max(1, min(page or 1, last_page))
        
        # Calcula offset e limit
        offset = (current_page - 1) * per_page
        
        # Obtém os dados para a página atual
        data = list(self.queryset.skip(offset).limit(per_page))
        
        # Calcula valores 'from' e 'to' (baseado em 1)
        from_index = offset + 1 if data else 0
        to_index = offset + len(data) if data else 0
        
        # Constrói resposta de paginação
        pagination_data = {
            "total": self.total,
            "per_page": per_page,
            "current_page": current_page,
            "last_page": last_page,
            "first_page_url": f"{self.base_url}?page=1&limit={per_page}",
            "last_page_url": f"{self.base_url}?page={last_page}&limit={per_page}",
            "next_page_url": f"{self.base_url}?page={current_page + 1}&limit={per_page}" if current_page < last_page else None,
            "prev_page_url": f"{self.base_url}?page={current_page - 1}&limit={per_page}" if current_page > 1 else None,
            "path": self.base_url,
            "from": from_index,
            "to": to_index,
            "items": [self._serialize_with_serializer(doc) for doc in data]
        }
        
        return pagination_data
    
    def _serialize_document(self, document: Document) -> Dict[str, Any]:
        """
        Converte documento MongoEngine para dicionário.
        Sobrescreva este método para serialização customizada.
        
        Args:
            document: Instância do documento MongoEngine
            
        Returns:
            Representação em dicionário do documento
        """
        return document.to_mongo().to_dict()
    
    def set_serializer(self, serializer_class):
        """
        Define um serializer personalizado para usar na serialização dos documentos.
        
        Args:
            serializer_class: Classe do serializer do Django REST Framework
        """
        self.serializer_class = serializer_class
        return self
    
    def _serialize_with_serializer(self, document: Document) -> Dict[str, Any]:
        """
        Serializa documento usando serializer do Django REST Framework.
        
        Args:
            document: Instância do documento MongoEngine
            
        Returns:
            Dados serializados pelo serializer
        """
        if hasattr(self, 'serializer_class') and self.serializer_class is not None:
            serializer = self.serializer_class(document)
            return serializer.data
        return self._serialize_document(document)


# Alternativa: Classe mixin
class PaginationMixin:
    """
    Classe mixin que pode ser adicionada às classes Document do MongoEngine para adicionar suporte à paginação.
    """
    
    @classmethod
    def paginate(cls, page: int = 1, per_page: int = 15, base_url: str = "http://localhost", 
                 query_filter: Optional[Dict] = None, serializer_class=None) -> Dict[str, Any]:
        """
        Pagina documentos com paginação no estilo Laravel.
        
        Args:
            page: Número da página atual (baseado em 1)
            per_page: Número de itens por página
            base_url: URL base para links de paginação
            query_filter: Dicionário de filtros opcional para consulta
            serializer_class: Classe do serializer para serialização customizada
            
        Returns:
            Dicionário contendo dados de paginação e resultados
        """
        # Constrói queryset
        if query_filter:
            queryset = cls.objects.filter(**query_filter)
        else:
            queryset = cls.objects.all()
        
        # Cria paginador e retorna resultados
        paginator = Paginator(queryset, per_page, base_url)
        if serializer_class:
            paginator.set_serializer(serializer_class)
        return paginator.paginate(page)


# Exemplos de uso:

# Exemplo 1: Usando a classe Paginator independente com serializer
"""
from .serializers import VehicleSerializer
from .models import Vehicle

# Cria paginador
vehicles_queryset = Vehicle.objects.all()
paginator = Paginator(vehicles_queryset, per_page=10, base_url="https://myapp.com/vehicles")

# Define o serializer
paginator.set_serializer(VehicleSerializer)

# Obtém página 1 com dados serializados
page_1_data = paginator.paginate(page=1)
print(page_1_data)
"""

# Exemplo 2: Usando a abordagem mixin com serializer
"""
from .serializers import VehicleSerializer

class Vehicle(Document, PaginationMixin):
    name = StringField(required=True)
    brand = StringField()
    year = IntegerField()

# Pagina diretamente do modelo com serializer
page_data = Vehicle.paginate(
    page=1, 
    per_page=10, 
    base_url="https://myapp.com/vehicles",
    serializer_class=VehicleSerializer
)

# Com filtros e serializer
filtered_page_data = Vehicle.paginate(
    page=1, 
    per_page=10, 
    base_url="https://myapp.com/vehicles",
    query_filter={'year__gte': 2020},
    serializer_class=VehicleSerializer
)
"""

# Exemplo 3: Serialização customizada herdando a classe
"""
from .serializers import VehicleSerializer

class VehiclePaginator(Paginator):
    def _serialize_document(self, document):
        # Usa sempre o VehicleSerializer
        serializer = VehicleSerializer(document)
        return serializer.data

# Usa paginador customizado
paginator = VehiclePaginator(Vehicle.objects.all(), per_page=10)
result = paginator.paginate(page=1)
"""

# Exemplo 4: Usando em Views do Django REST Framework
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vehicle
from .serializers import VehicleSerializer

@api_view(['GET'])
def list_vehicles(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 15))
    
    # Opção 1: Usando Paginator diretamente
    paginator = Paginator(Vehicle.objects.all(), per_page=per_page, 
                         base_url=request.build_absolute_uri().split('?')[0])
    paginator.set_serializer(VehicleSerializer)
    result = paginator.paginate(page=page)
    
    # Opção 2: Usando mixin (se Vehicle herdar de PaginationMixin)
    # result = Vehicle.paginate(page=page, per_page=per_page, 
    #                          base_url=request.build_absolute_uri().split('?')[0],
    #                          serializer_class=VehicleSerializer)
    
    return Response(result)
"""