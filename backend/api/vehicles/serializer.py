from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Vehicle

class VehicleSerializer(DocumentSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
