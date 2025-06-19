
"""
Views for the Trips API.
This module contains the views for handling trip-related API requests.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, ParseError
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from bson import ObjectId
from trips.serializers import TripSerializer, TripListSerializer, TripListSerializerById, TripListParamsSerializer
from core.utils.pagination import Paginator
from rest_framework import serializers
from rest_framework.reverse import reverse
from datetime import datetime, timezone
from vehicles.models import Vehicle
from trips.models import Trip
from users.authentication import MongoJWTAuthentication

@api_view(['GET'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def list_trips(request):
    """List all trips with optional filtering and pagination."""
    # Validar parâmetros da requisição
    params_serializer = TripListParamsSerializer(data=request.query_params)
    params_serializer.is_valid(raise_exception=True)
    
    # Obter parâmetros
    page = params_serializer.validated_data['page']
    limit = params_serializer.validated_data['limit']
    destination = params_serializer.validated_data.get('destination')

    # Construir a query
    query = {'trips__deleted': False}
    if destination:
        query['trips__destination__icontains'] = destination
    
    # Buscar os veículos que contêm viagens que atendem aos filtros
    vehicles = Vehicle.objects(**query)
    
    # Coletar e filtrar as viagens
    all_trips = []
    for vehicle in vehicles:
        trips = [t for t in vehicle.trips if not t.deleted]
        if destination:
            trips = [t for t in trips if destination.lower() in t.destination.lower()]
        all_trips.extend(trips)
    
    # Ordenar as viagens por data (mais recentes primeiro)
    all_trips.sort(key=lambda x: x.createdAt, reverse=True)
    
    # Aplicar paginação
    total = len(all_trips)
    total_pages = (total + limit - 1) // limit if limit > 0 else 1
    
    # Garantir que a página solicitada existe
    page = min(page, max(1, total_pages))
    
    start = (page - 1) * limit
    end = start + limit
    paginated_trips = all_trips[start:end]
    
    # Se não houver itens na página solicitada, retornar array vazio
    if not paginated_trips and page > 1:
        paginated_trips = []
    
    # Construir as URLs de navegação
    base_url = request.build_absolute_uri(request.path)
    
    response_data = {
        'total': total,
        'per_page': limit,
        'current_page': page,
        'last_page': total_pages,
        'first_page_url': f"{base_url}?page=1&limit={limit}",
        'last_page_url': f"{base_url}?page={total_pages}&limit={limit}",
        'next_page_url': f"{base_url}?page={page + 1}&limit={limit}" if page < total_pages else None,
        'prev_page_url': f"{base_url}?page={page - 1}&limit={limit}" if page > 1 else None,
        'path': base_url,
        'from': start + 1 if total > 0 else 0,
        'to': min(end, total),
        'items': TripListSerializer(paginated_trips, many=True).data
    }
    
    return Response(response_data)

@api_view(['GET'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def get_trip(request, trip_id):
    """Get trip by id."""
    try:
        # Busca o veículo que contém a viagem
        vehicle = Vehicle.objects(trips__id=ObjectId(trip_id)).first()
        if not vehicle:
            raise NotFound('Viagem não encontrada')
            
        # Encontra a viagem específica dentro do veículo
        trip = next((t for t in vehicle.trips if not t.deleted and str(t.id) == trip_id), None)
        if not trip:
            raise NotFound('Viagem não encontrada')
                
        if not trip:
            raise NotFound('Viagem não encontrada')
            
        return Response(TripListSerializerById(trip).data)
    except Exception as e:
        raise NotFound('Erro ao buscar viagem')

@api_view(['DELETE'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_trip(request, trip_id):
    """Delete a trip."""
    try:
        # Tenta converter o ID para ObjectId
        try:
            trip_oid = ObjectId(trip_id)
        except Exception:
            raise NotFound('ID de viagem inválido')
            
        # Busca o veículo que contém a viagem
        vehicle = Vehicle.objects(trips__id=trip_oid).first()
        if not vehicle:
            raise NotFound('Viagem não encontrada')
            
        # Encontra a viagem específica dentro do veículo
        trip = next((t for t in vehicle.trips if not t.deleted and str(t.id) == trip_id), None)
        if not trip:
            raise NotFound('Viagem não encontrada ou já foi excluída')
            
        # Marca a viagem como deletada
        trip.deleted = True
        trip.deletedAt = datetime.now(timezone.utc)
        vehicle.save()
        
        return Response({'message': 'Viagem deletada com sucesso'}, status=status.HTTP_200_OK)
    except NotFound as e:
        # Propaga erros NotFound diretamente
        raise
    except Exception as e:
        # Para outros erros, logamos e retornamos um erro genérico
        print(f"Erro ao deletar viagem: {str(e)}")
        raise ParseError('Ocorreu um erro ao processar a requisição')

@api_view(['POST'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def create_trip(request):
    """Criar viagem."""
    try:
        vehicle_id = ObjectId(request.data['vehicleId'])
        vehicle = Vehicle.objects.get(id=vehicle_id)
    except Vehicle.DoesNotExist:
        raise NotFound('Veículo não encontrado')
    except Exception:
        raise ParseError('ID do veículo inválido')
    
    # Valida os dados da viagem
    serializer = TripSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # Cria e adiciona a nova viagem ao veículo
    trip = Trip(**serializer.validated_data)
    vehicle.trips.append(trip)
    vehicle.save()

    return Response(TripSerializer(trip).data, status=status.HTTP_201_CREATED)

# bruno
@api_view(['PUT'])
@authentication_classes([MongoJWTAuthentication])
@permission_classes([IsAuthenticated])
def update_trip(request, trip_id):
    """Atualiza uma viagem específica"""
    try:
        # Busca a viagem específica no veículo
        vehicle = Vehicle.objects.get(trips__id=trip_id)
        trip = vehicle.trips.get(id=trip_id)
    except Vehicle.DoesNotExist:
        raise NotFound('Veículo não encontrado')
    except Trip.DoesNotExist:
        raise NotFound('Viagem não existe neste veículo')
        
    # Valida e aplica atualizações
    serializer = TripSerializer(trip, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    
    # Salva alterações
    for key, value in serializer.validated_data.items():
        setattr(trip, key, value)
    vehicle.save()
    
    return Response(serializer.data)