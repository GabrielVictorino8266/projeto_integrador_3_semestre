from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer
from .models import Trip

class TripSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Trip
        fields = '__all__'