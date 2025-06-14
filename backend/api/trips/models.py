from mongoengine import Document, StringField, DateTimeField, BooleanField
from datetime import datetime

class Trip(Document):
    """Trip document class with common fields."""
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    deleted = BooleanField(default=False)
    deleted_at = DateTimeField(required=False)