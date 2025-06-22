from django.db.models import TextChoices

class TripStatus(TextChoices):
    SCHEDULED = "scheduled", "Programado"
    CANCELLED = "cancelled", "Cancelado"
    IN_PROGRESS = "in_progress", "Em Andamento"
    COMPLETED = "completed", "Concluído"