from rest_framework import serializers
from .vehicle_types import VehicleTypes

class VehicleSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True),
    numeroVeiculo = serializers.CharField(max_length=10),
    placa = serializers.CharField(max_length=8),
    tipoVeiculo = serializers.ChoiceField(choices=VehicleTypes.choices),
    anoFabricacao = serializers.IntegerField(),
    marca = serializers.CharField(max_length=20),
    kmAtual = serializers.IntegerField(),
    limiteAvisoKm = serializers.IntegerField(),
