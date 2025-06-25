from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer
from .models import Trip
from drivers.models import Driver
from rest_framework import serializers
from vehicles.models import Vehicle
class TripListParamsSerializer(serializers.Serializer):
    page = serializers.IntegerField(min_value=1, default=1)
    limit = serializers.IntegerField(min_value=1, max_value=100, default=10)
    destination = serializers.CharField(required=False, allow_blank=True)
    status = serializers.CharField(required=False, allow_blank=True)

class TripSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

class TripListSerializer(EmbeddedDocumentSerializer):
    driverName = serializers.SerializerMethodField()
    vehicleLicensePlate = serializers.SerializerMethodField()
    vehicleId = serializers.SerializerMethodField()
    
    class Meta:
        model = Trip
        fields = '__all__'
        extra_kwargs = {
            'driverId': {'required': False},
            'startDateTime': {'required': False},
            'origin': {'required': False},
            'destination': {'required': False},
            'initialKm': {'required': False}
        }
    
    def get_driverName(self,obj):
        try:
            driver = Driver.objects.get(id=obj.driverId)
            return driver.name
        except Driver.DoesNotExist:
            return None
    
    def get_vehicleLicensePlate(self, obj):
        try:
            # Tenta obter a placa do veículo do documento pai
            if hasattr(obj, '_instance') and obj._instance:
                return obj._instance.licensePlate
            # Se não tiver documento pai, tenta pelo vehicleId
            if hasattr(obj, 'vehicleId') and obj.vehicleId:
                vehicle = Vehicle.objects.get(id=obj.vehicleId)
                return vehicle.licensePlate
            return None
        except (Vehicle.DoesNotExist, AttributeError):
            return None
    
    def get_vehicleId(self, obj):
        # Retorna o ID do veículo pai se disponível
        if hasattr(obj, '_instance') and obj._instance:
            return str(obj._instance.id)
        # Se existir um vehicleId no documento da viagem, retorna ele
        if hasattr(obj, 'vehicleId') and obj.vehicleId:
            return str(obj.vehicleId)
        return None

class TripListSerializerById(EmbeddedDocumentSerializer):
    driverName = serializers.SerializerMethodField()
    vehicleLicensePlate = serializers.SerializerMethodField()
    vehicleId = serializers.SerializerMethodField()

    class Meta:
        model = Trip
        fields = ['id', 'driverId','driverName', 'startDateTime', 'origin', 'destination', 'initialKm', 'finalKm', 'completed', 'status', 'vehicleId', 'vehicleLicensePlate']
        extra_kwargs = {
            'driverId': {'required': False},
            'startDateTime': {'required': False},
            'origin': {'required': False},
            'destination': {'required': False},
            'initialKm': {'required': False}
        }
    
    def get_driverName(self,obj):
        try:
            driver = Driver.objects.get(id=obj.driverId)
            return driver.name
        except Driver.DoesNotExist:
            return None
    
    def get_vehicleLicensePlate(self, obj):
        try:
            # Tenta obter a placa do veículo do documento pai
            if hasattr(obj, '_instance') and obj._instance:
                return obj._instance.licensePlate
            # Se não tiver documento pai, tenta pelo vehicleId
            if hasattr(obj, 'vehicleId') and obj.vehicleId:
                vehicle = Vehicle.objects.get(id=obj.vehicleId)
                return vehicle.licensePlate
            return None
        except (Vehicle.DoesNotExist, AttributeError):
            return None
    
    def get_vehicleId(self, obj):
        # Retorna o ID do veículo pai se disponível
        if hasattr(obj, '_instance') and obj._instance:
            return str(obj._instance.id)
        # Se existir um vehicleId no documento da viagem, retorna ele
        if hasattr(obj, 'vehicleId') and obj.vehicleId:
            return str(obj.vehicleId)
        return None
        