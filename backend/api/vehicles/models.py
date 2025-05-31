from mongoengine import Document, StringField, IntField
from .vehicle_types import VehicleTypes

class Vehicle(Document):
    numeroVeiculo = StringField(max_length=10, required=True)
    placa = StringField(max_length=8, required=True)
    tipoVeiculo = StringField(choices=VehicleTypes.values, required=True)
    anoFabricacao = IntField(required=True)
    marca = StringField(max_length=20, required=True)
    kmAtual = IntField(required=True)
    limiteAvisoKm = IntField(required=True)
