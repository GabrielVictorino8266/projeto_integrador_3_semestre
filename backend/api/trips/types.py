from django.db.models import TextChoices

class TripStatus(TextChoices):
    ACTIVE = "active", "Ativo"
    CANCELLED = "cancelled", "Cancelado"
    IN_PROGRESS = "in_progress", "Em andamento"