from mongoengine import Document, StringField, IntField, ListField, DateField, BooleanField
import datetime

class Driver(Document):
    password = StringField(required=True)
    cpf = StringField(required=True, unique=True)
    email = StringField(required=True)
    name =StringField(required=True)
    birthYear = DateField(required=True)
    phone = StringField(required=True)
    licenseType = StringField(required=True)
    licenseNumber = StringField(required=True)
    performance = IntField(default=0)
    incidents = ListField(default=[])
    isActive = BooleanField(default=True)
    type = StringField(default='Motorista')

    meta = {'collection': 'users'}
