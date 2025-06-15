from celery import shared_task
from django.core.management import call_command
from datetime import timedelta
from celery.schedules import crontab
from datetime import datetime, timezone

@shared_task
def cleanup_tokens():
    """
    Task to cleanup expired tokens.
    Runs every day at midnight.
    """
    call_command('cleanup_tokens')

# Schedule the task to run daily at midnight
cleanup_tokens.apply_async(
    eta=(datetime.now() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
)
