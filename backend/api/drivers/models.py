from mongoengine import Document, StringField, IntField, ListField, ReferenceField, BooleanField
import datetime

class Driver(Document):
    password = StringField(required=True)
    cpf = StringField(required=True, unique=True)
    email = StringField(required=True)
    name =StringField(required=True)
    birthDate = datetime.date
    phone = StringField(required=True)
    licenseType = StringField(required=True)
    licenseNumber = StringField(required=True)
    performance = IntField(default=0)
    incidents = ListField(StringField(), default=[])
    isActive = BooleanField(default=True)
    type = StringField(default='Motorista')
