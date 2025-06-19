from mongoengine import StringField, DateTimeField, BooleanField, EmbeddedDocument, FloatField
from datetime import datetime, timezone
from .types import TripStatus
from mongoengine.errors import ValidationError
from mongoengine import ObjectIdField
from bson import ObjectId

class Trip(EmbeddedDocument):
    """Modelo de viagem."""
    id = ObjectIdField(primary_key=True, default=ObjectId, unique=True, required=True)
    driverId = ObjectIdField(required=True)
    startDateTime = DateTimeField(required=True)
    endDateTime = DateTimeField(default=None)
    origin = StringField(required=True)
    destination = StringField(required=True)
    initialKm = FloatField(min_value=0, required=True)
    finalKm = FloatField(min_value=0, default=None)
    completed = BooleanField(required=True, default=False)
    deleted = BooleanField(default=False)
    status = StringField(choices=TripStatus.values, required=True, default=TripStatus.ACTIVE)
    createdAt = DateTimeField(required=True, default=datetime.now(timezone.utc))
    updatedAt = DateTimeField(required=True, default=datetime.now(timezone.utc))
    deletedAt = DateTimeField(default=None)

    def clean(self):
        # Converte datetimes sem timezone (naive) para com timezone (UTC) se necessário
        if self.startDateTime and not self.startDateTime.tzinfo:
            self.startDateTime = self.startDateTime.replace(tzinfo=timezone.utc)
        if self.endDateTime and not self.endDateTime.tzinfo:
            self.endDateTime = self.endDateTime.replace(tzinfo=timezone.utc)
            
        # Valida a ordem das datas
        if self.startDateTime and self.endDateTime and self.endDateTime < self.startDateTime:
            raise ValidationError('A data/hora final deve ser posterior à data/hora inicial')