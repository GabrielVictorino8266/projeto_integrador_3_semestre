from mongoengine import ValidationError
from vehicles.models import Vehicle
from vehicles.types import VehicleTypes
from .vehicle_test_case import VehicleTestCase

class VehicleModelTest(VehicleTestCase):
    def test_valid_vehicle_creation(self):
        """
        Testa a criação válida de um veículo.
        """
        vehicle = Vehicle(**self.valid_vehicle_data)
        try:
            vehicle.validate()
        except ValidationError as e:
            self.fail(f'validate() raised ValidationError unexpectedly: {e}')

    def test_vehicle_save_and_retrieve(self):
        """
        Testa a persistência e recuperação de um veículo no banco.
        """
        vehicle = Vehicle(**self.valid_vehicle_data)
        vehicle.save()
        retrieved_vehicle = Vehicle.objects.get(vehicleNumber='12345')
        self.assertEqual(retrieved_vehicle.licensePlate, 'ABC1234')
        self.assertEqual(retrieved_vehicle.vehicleType, VehicleTypes.CARRO)

    def test_required_fields_validation(self):
        """
        Testa validação dos campos obrigatórios.
        """
        vehicle = Vehicle()
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        error_message = str(cm.exception)
        required_fields = ['vehicleNumber', 'licensePlate', 'vehicleType']
        for field in required_fields:
            self.assertIn(field, error_message)

    def test_vehicle_number_max_length(self):
        """
        Testa validação do comprimento máximo do campo vehicleNumber.
        """
        data = self.valid_vehicle_data.copy()
        data['vehicleNumber'] = 'X' * 999
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        self.assertIn('vehicleNumber', str(cm.exception))

    def test_license_plate_format_validation(self):
        """
        Testa validação do formato do campo licensePlate.
        """
        data = self.valid_vehicle_data.copy()
        data['licensePlate'] = 'INVALID'
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError):
            vehicle.validate()

    def test_vehicle_type_invalid_choice(self):
        """
        Testa validação para escolha inválida em vehicleType.
        """
        data = self.valid_vehicle_data.copy()
        data['vehicleType'] = 'invalid_choice'
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        self.assertIn('vehicleType', str(cm.exception))

    def test_manufacturing_year_range(self):
        """
        Testa validação do intervalo permitido para manufacturingYear.
        """
        data = self.valid_vehicle_data.copy()
        data['manufacturingYear'] = 1800
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError):
            vehicle.validate()

    def test_current_km_negative(self):
        """
        Testa que currentKm não aceita valores negativos.
        """
        data = self.valid_vehicle_data.copy()
        data['currentKm'] = -1000
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError):
            vehicle.validate()

    def test_invalid_deleted_at(self):
        """
        Testa validação para deletedAt inválido.
        """
        data = self.valid_vehicle_data.copy()
        data['deletedAt'] = 'invalid_date'
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        self.assertIn('deletedAt', str(cm.exception))

    def test_invalid_status(self):
        """
        Testa validação para escolha inválida em status.
        """
        data = self.valid_vehicle_data.copy()
        data['status'] = 'invalid_status'
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        self.assertIn('status', str(cm.exception))