"""
    Serializers for the Drivers API.
    This module contains the serializers for handling driver-related API requests.
"""

from rest_framework import serializers
from datetime import datetime, date
import re


class DriverSerializer(serializers.Serializer):
    """
    Serializer for driver data.
    """
    id = serializers.IntegerField(required=False, read_only=True)
    name = serializers.CharField(
        max_length=200,
        required=True,
        help_text="Driver's name",
        error_messages={
            'required': 'Driver name is required.',
            'max_length': 'Driver name cannot exceed 200 characters.',
            'blank': 'Driver name cannot be blank.'
        }
    )
    cpf = serializers.CharField(
        max_length=11,
        required=True,
        help_text="Driver's CPF (Cadastro de Pessoas Físicas)",
        error_messages={
            'required': 'Driver CPF is required.',
            'max_length': 'Driver CPF must be 11 characters long.',
            'blank': 'Driver CPF cannot be blank.'
        }
    )
    birth_date = serializers.DateField(
        required=True,
        help_text="Driver's birth date (YYYY-MM-DD)",
        error_messages={
            'required': 'Driver birth date is required.',
            'invalid': 'Invalid date format. Use YYYY-MM-DD.',
            'blank': 'Driver birth date cannot be blank.'
        }
    )
    phone = serializers.CharField(
        max_length=15,
        required=False,
        help_text="Driver's phone number",
        error_messages={
            'max_length': 'Driver phone number cannot exceed 15 characters.',
            'blank': 'Driver phone number can be blank.'
        }
    )
    email = serializers.EmailField(
        required=False,
        help_text="Driver's email address",
        error_messages={
            'invalid': 'Invalid email format.',
            'blank': 'Driver email can be blank.'
        }
    )
    address = serializers.CharField(
        max_length=255,
        required=False,
        help_text="Driver's address",
        error_messages={
            'max_length': 'Driver address cannot exceed 255 characters.',
            'blank': 'Driver address can be blank.'
        }
    )
    cnh_number = serializers.CharField(
        max_length=11,
        required=True,
        help_text="Driver's CNH (Carteira Nacional de Habilitação) number",
        error_messages={
            'required': 'Driver CNH number is required.',
            'max_length': 'Driver CNH number must be 11 characters long.',
            'blank': 'Driver CNH number cannot be blank.'
        }
    )
    cnh_category = serializers.ChoiceField(
        choices=[
            ('A', 'Categoria A'),
            ('B', 'Categoria B'),
            ('C', 'Categoria C'),
            ('D', 'Categoria D'),
            ('E', 'Categoria E'),
            ('AB', 'Categoria AB'),
            ('AC', 'Categoria AC'),
            ('AD', 'Categoria AD'),
            ('AE', 'Categoria AE'),
        ],
        required=True,
        help_text="Categoria da CNH",
        error_messages={
            'required': 'Categoria da CNH é obrigatória.',
            'invalid_choice': 'Categoria da CNH inválida.'
        }
    )
    is_active = serializers.BooleanField(
        default=True,
        help_text="Indicates if the driver is currently active",
    )
    created_at = serializers.DateTimeField(
        default=datetime.now,
        read_only=True,
        help_text="Timestamp when the driver was created"
    )
    updated_at = serializers.DateTimeField(
        default=datetime.now,
        read_only=True,
        help_text="Timestamp when the driver was last updated"
    )

    def validate_name(self, value):
        """
        Validate the driver's name.
        """
        if not value.strip():
            raise serializers.ValidationError("Driver name cannot be blank.")

        separated_name = value.strip().split()
        if len(separated_name) < 2:
            raise serializers.ValidationError("Driver name must contain at least a first and last name.")
        
        return value.strip().title()
    
    def validate_cpf(self, value):
        """
        Validate the driver's CPF.
        """
        cpf_clean = re.sub(r'[^0-9]', '', value)
        if len(cpf_clean) != 11 or not cpf_clean.isdigit():
            raise serializers.ValidationError("Driver CPF must be 11 digits long and contain only numbers.")
        
        if cpf_clean == cpf_clean[0] * 11:
            raise serializers.ValidationError("Driver CPF cannot be all the same digit.")
        
        return cpf_clean
    
    def validate_cnh_number(self, value):
        """
        Validate the driver's CNH number.
        """
        cnh_clean = re.sub(r'[^0-9]', '', value)
        if len(cnh_clean) != 11:
            raise serializers.ValidationError("Driver CNH number must be 11 digits long.")

        return cnh_clean
    
    def validate_phone(self, value):
        """
        Validate the driver's phone number.
        """
        phone_clean = re.sub(r'[^0-9]', '', value)

        if len(phone_clean) < 10 or len(phone_clean) > 11:
            raise serializers.ValidationError("Driver phone number must be between 10 and 15 digits long.")
    
        # Format phone
        if len(phone_clean) == 10:
            return f"({phone_clean[:2]}) {phone_clean[2:6]}-{phone_clean[6:]}"
        else:
            return f"({phone_clean[:2]}) {phone_clean[2:7]}-{phone_clean[7:]}"
        
    def validate_birth_date(self, value):
        """
        Validate the driver's birth date.
        """
        if value > date.today():
            raise serializers.ValidationError("Driver's birth date cannot be in the future.")
        
        return value
    
class DriverDashboardSerializer(serializers.Serializer):
    """
    Serializer for driver dashboard data.
    """
    total_drivers = serializers.IntegerField(read_only=True, help_text="Total number of drivers")
    active_drivers = serializers.IntegerField(read_only=True, help_text="Number of active drivers")
    inactive_drivers = serializers.IntegerField(read_only=True, help_text="Number of inactive drivers")

    def get_total_drivers(self, obj):
        """
        Get the total number of drivers.
        """
        return obj.get('total_drivers', 0)

    def get_active_drivers(self, obj):
        """
        Get the number of active drivers.
        """
        return obj.get('active_drivers', 0)

    def get_inactive_drivers(self, obj):
        """
        Get the number of inactive drivers.
        """
        return obj.get('inactive_drivers', 0)



class ErrorResponseSerializer(serializers.Serializer):
    """
    Serializer padrão para respostas de erro.
    """
    success = serializers.BooleanField(default=False)
    error = serializers.CharField()
    details = serializers.DictField(required=False)


class SuccessResponseSerializer(serializers.Serializer):
    """
    Serializer padrão para respostas de sucesso.
    """
    success = serializers.BooleanField(default=True)
    message = serializers.CharField(required=False)
    data = serializers.DictField(required=False)