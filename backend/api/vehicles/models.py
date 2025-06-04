from mongoengine import DateTimeField, Document, StringField, IntField
from .types import VehicleTypes, VehicleStatus
import datetime

class Vehicle(Document):
    vehicleNumber = StringField(max_length=10, required=True)
    licensePlate = StringField(max_length=8, required=True, regex=r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$', pre_save=lambda s: s.upper() if s else None)
    vehicleType = StringField(choices=VehicleTypes.values, required=True)
    manufacturingYear = IntField(min_value=1900, max_value=datetime.date.today().year, required=True)
    brand = StringField(max_length=20, required=True)
    currentKm = IntField(min_value=0, required=True)
    warningKmLimit = IntField(min_value=0, required=True)
    deletedAt = DateTimeField(null=True)
    status = StringField(choices=VehicleStatus.values, default=VehicleStatus.ACTIVE)
