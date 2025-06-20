from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer
from .models import Trip
from drivers.models import Driver
from rest_framework import serializers

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

class TripListSerializerById(EmbeddedDocumentSerializer):
    driverName = serializers.SerializerMethodField()
    
    class Meta:
        model = Trip
        fields = ['id', 'driverName', 'startDateTime', 'origin', 'destination', 'initialKm', 'finalKm', 'completed', 'status']
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