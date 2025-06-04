from mongoengine import DateTimeField, Document, StringField, IntField
from .vehicle_types import VehicleTypes
import datetime

class Vehicle(Document):
    numeroVeiculo = StringField(max_length=10, required=True)
    placa = StringField(max_length=8, required=True, regex=r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$', pre_save=lambda s: s.upper() if s else None)
    tipoVeiculo = StringField(choices=VehicleTypes.values, required=True)
    anoFabricacao = IntField(min_value=1900, max_value=datetime.date.today().year, required=True)
    marca = StringField(max_length=20, required=True)
    kmAtual = IntField(min_value=0, required=True)
    limiteAvisoKm = IntField(min_value=0, required=True)
    dataExclusao = DateTimeField(null=True)
