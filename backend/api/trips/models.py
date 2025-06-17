from mongoengine import StringField, DateTimeField, BooleanField, EmbeddedDocument, FloatField
from datetime import datetime, timezone
from .types import TripStatus
from mongoengine.errors import ValidationError
from mongoengine import ObjectIdField

class Trip(EmbeddedDocument):
    """Modelo de viagem."""
    driverId = ObjectIdField(required=True)
    startDateTime = DateTimeField(required=True)
    endDateTime = DateTimeField(default=None)
    origin = StringField(required=True)
    destination = StringField(required=True)
    initialKm = FloatField(required=True)
    finalKm = FloatField(default=None)
    completed = BooleanField(required=True, default=False)
    status = StringField(choices=TripStatus.values, required=True, default=TripStatus.ACTIVE)
    createdAt = DateTimeField(required=True, default=datetime.now(timezone.utc))
    updatedAt = DateTimeField(required=True, default=datetime.now(timezone.utc))
    deletedAt = DateTimeField(default=None)

    def clean(self):
        """Garantir que endDateTime seja maior que startDateTime"""
        if self.endDateTime and self.startDateTime and self.endDateTime < self.startDateTime:
            raise ValidationError('Data final deve ser maior que a data inicial')