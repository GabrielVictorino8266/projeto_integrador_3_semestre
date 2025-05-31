from django.db import models
from .vehicle_types import VehicleTypes

    
# Create your models here.
class Vehicle(models.Model):
    numeroVeiculo = models.CharField(max_length=10)
    placa = models.CharField(max_length=8)
    tipoVeiculo = models.CharField(max_length=20, choices=VehicleTypes.choices)
    anoFabricacao = models.IntegerField()
    marca = models.CharField(max_length=20)
    kmAtual = models.IntegerField()
    limiteAvisoKm = models.IntegerField()