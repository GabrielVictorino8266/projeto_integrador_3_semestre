from django.core.management.base import BaseCommand
from users.auth_services import cleanup_expired_tokens
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Cleanup expired JWT tokens'

    def handle(self, *args, **options):
        """
        Cleanup expired tokens from the database.
        """
        try:
            # Log cleanup start
            logger.info("Starting token cleanup...")
            
            # Perform cleanup
            result = cleanup_expired_tokens()
            
            if result:
                logger.info("Token cleanup completed successfully")
            else:
                logger.error("Token cleanup failed")
                
        except Exception as e:
            logger.error(f"Error during token cleanup: {str(e)}")
            raise
