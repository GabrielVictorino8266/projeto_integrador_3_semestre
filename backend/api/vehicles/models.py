from django.db import models
from .vehicle_types import VehicleTypes

    
# Create your models here.
class Vehicle(models.Model):
    numero_veiculo = models.CharField(max_length=10)
    placa = models.CharField(max_length=8)
    tipo_veiculo = models.CharField(max_length=20, choices=VehicleTypes.choices)
    ano_fabricacao = models.IntegerField()
    marca = models.CharField(max_length=20)
    km_atual = models.IntegerField()
    limite_aviso_km = models.IntegerField()