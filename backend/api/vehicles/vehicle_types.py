from django.db.models import TextChoices

class VehicleTypes(TextChoices):
    CARRO = 'carro', 'Carro'
    MOTO = 'moto', 'Moto'
    CAMINHAO = 'caminhao', 'Caminhão'
    ONIBUS = 'onibus', 'Onibus'