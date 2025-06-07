from django.db.models import TextChoices

class VehicleTypes(TextChoices):
    CARRO = 'carro', 'Carro'
    MOTO = 'moto', 'Moto'
    CAMINHAO = 'caminhao', 'Caminhão'
    ONIBUS = 'onibus', 'Onibus'

class VehicleStatus(TextChoices):
    ACTIVE = 'active', 'Ativo'
    INACTIVE = 'inactive', 'Inativo'