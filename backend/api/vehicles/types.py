from django.db.models import TextChoices

class VehicleTypes(TextChoices):
    CARRO = 'carro', 'Carro'
    MOTO = 'moto', 'Moto'
    CAMINHAO = 'caminhao', 'Caminhão'
    ONIBUS = 'onibus', 'Onibus'
    VAN = 'van', 'Van'

class VehicleStatus(TextChoices):
    ACTIVE = 'active', 'Ativo'
    INACTIVE = 'excluido', 'Excluído'
    MAINTENANCE = 'maintenance', 'Manutenção'
    NOT_AVAILABLE = 'indisponivel', 'Indisponível'