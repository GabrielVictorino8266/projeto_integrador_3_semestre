from django.test import TestCase
from mongoengine import ValidationError, connection
from vehicles.models import Vehicle
from vehicles.vehicle_types import VehicleTypes
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
        retrieved_vehicle = Vehicle.objects.get(numeroVeiculo='12345')
        self.assertEqual(retrieved_vehicle.placa, 'ABC1234')
        self.assertEqual(retrieved_vehicle.tipoVeiculo, VehicleTypes.CARRO)

    def test_required_fields_validation(self):
        """
        Testa validação dos campos obrigatórios.
        """
        vehicle = Vehicle()
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        error_message = str(cm.exception)
        required_fields = ['numeroVeiculo', 'placa', 'tipoVeiculo']
        for field in required_fields:
            self.assertIn(field, error_message)

    def test_numero_veiculo_max_length(self):
        """
        Testa validação do comprimento máximo do campo numeroVeiculo.
        """
        data = self.valid_vehicle_data.copy()
        data['numeroVeiculo'] = 'X' * 999
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        self.assertIn('numeroVeiculo', str(cm.exception))

    def test_placa_format_validation(self):
        """
        Testa validação do formato do campo placa.
        """
        data = self.valid_vehicle_data.copy()
        data['placa'] = 'INVALID'
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError):
            vehicle.validate()

    def test_tipo_veiculo_invalid_choice(self):
        """
        Testa validação para escolha inválida em tipoVeiculo.
        """
        data = self.valid_vehicle_data.copy()
        data['tipoVeiculo'] = 'invalid_choice'
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        self.assertIn('tipoVeiculo', str(cm.exception))

    def test_ano_fabricacao_range(self):
        """
        Testa validação do intervalo permitido para anoFabricacao.
        """
        data = self.valid_vehicle_data.copy()
        data['anoFabricacao'] = 1800
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError):
            vehicle.validate()

    def test_km_atual_negative(self):
        """
        Testa que kmAtual não aceita valores negativos.
        """
        data = self.valid_vehicle_data.copy()
        data['kmAtual'] = -1000
        vehicle = Vehicle(**data)
        with self.assertRaises(ValidationError):
            vehicle.validate()