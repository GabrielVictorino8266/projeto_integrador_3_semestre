from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from users.authentication import SimpleUser
from .vehicle_types import VehicleTypes
from .models import Vehicle
from mongoengine import ValidationError
from django.urls import reverse

class VehicleAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # Dados de usuário simulados
        self.mock_user_data = {
            '_id': '507f1f77bcf86cd799439011',
            'email': 'test@example.com',
            'name': 'Test User',
            'role': 'user'
        }
        
        self.test_user = SimpleUser(self.mock_user_data)
        
        # Dados válidos base do veículo - reutilizáveis em todos os testes
        self.valid_vehicle_data = {
            'numeroVeiculo': '12345',
            'placa': 'ABC1234',
            'tipoVeiculo': VehicleTypes.CARRO,
            'anoFabricacao': 2020,
            'marca': 'Fiat',
            'kmAtual': 50000,
            'limiteAvisoKm': 10000
        }
        
        # Pré-autenticação para todos os testes da API
        self.client.force_authenticate(user=self.test_user)
        self.url = reverse('create_vehicle')

    def test_create_vehicle_success(self):
        """Testa criação bem-sucedida de veículo com dados válidos"""
        response = self.client.post(self.url, self.valid_vehicle_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Verificação mais concisa usando as chaves de response.data
        expected_fields = ['numeroVeiculo', 'placa', 'tipoVeiculo', 'anoFabricacao', 
                          'marca', 'kmAtual', 'limiteAvisoKm']
        
        for field in expected_fields:
            self.assertEqual(response.data[field], self.valid_vehicle_data[field])

    def test_create_vehicle_unauthenticated(self):
        """Testa que requisições não autenticadas são rejeitadas"""
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, self.valid_vehicle_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_vehicle_invalid_tipo_veiculo(self):
        """Testa erro de validação para tipo de veículo inválido"""
        invalid_data = self.valid_vehicle_data.copy()
        invalid_data['tipoVeiculo'] = 'invalid_choice'
        
        response = self.client.post(self.url, invalid_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Opcional: Verificar mensagem de erro específica
        self.assertIn('tipoVeiculo', response.data)

    def test_create_vehicle_missing_required_fields(self):
        """Testa erro de validação quando campos obrigatórios estão ausentes"""
        minimal_data = {'numeroVeiculo': '12345'}
        
        response = self.client.post(self.url, minimal_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        """Limpa dados após cada teste"""
        # Limpa veículos criados se usando banco de dados real
        Vehicle.objects.delete()


class VehicleModelTest(TestCase):
    def setUp(self):
        self.valid_vehicle_data = {
            'numeroVeiculo': '12345',
            'placa': 'ABC1234',
            'tipoVeiculo': VehicleTypes.CARRO,
            'anoFabricacao': 2020,
            'marca': 'Fiat',
            'kmAtual': 50000,
            'limiteAvisoKm': 10000
        }

    def test_valid_vehicle_creation(self):
        """Testa que dados válidos de veículo passam na validação"""
        vehicle = Vehicle(**self.valid_vehicle_data)
        
        # Não deve gerar ValidationError
        try:
            vehicle.validate()
        except ValidationError as e:
            self.fail(f'validate() gerou ValidationError inesperadamente: {e}')

    def test_vehicle_save_and_retrieve(self):
        """Testa salvamento e recuperação de um veículo"""
        vehicle = Vehicle(**self.valid_vehicle_data)
        vehicle.save()
        
        # Recupera e verifica
        retrieved_vehicle = Vehicle.objects.get(numeroVeiculo='12345')
        self.assertEqual(retrieved_vehicle.placa, 'ABC1234')
        self.assertEqual(retrieved_vehicle.tipoVeiculo, VehicleTypes.CARRO)

    def test_required_fields_validation(self):
        """Testa que campos obrigatórios ausentes geram ValidationError"""
        vehicle = Vehicle()
        
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        
        # Opcional: Verifica que campos obrigatórios específicos são mencionados
        error_message = str(cm.exception)
        # Ajustar nomes dos campos baseado nos requisitos do seu modelo
        required_fields = ['numeroVeiculo', 'placa', 'tipoVeiculo']
        for field in required_fields:
            self.assertIn(field, error_message)

    def test_numero_veiculo_max_length(self):
        """Testa validação de tamanho máximo do numeroVeiculo"""
        data = self.valid_vehicle_data.copy()
        data['numeroVeiculo'] = 'X' * 999  # Excede tamanho máximo
        
        vehicle = Vehicle(**data)
        
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        
        self.assertIn('numeroVeiculo', str(cm.exception))

    def test_placa_format_validation(self):
        """Testa validação de formato da placa se você tiver validação customizada"""
        data = self.valid_vehicle_data.copy()
        data['placa'] = 'INVALID'  # Formato inválido
        
        vehicle = Vehicle(**data)
        
        # Ajustar baseado se você tem validação de formato de placa
        with self.assertRaises(ValidationError):
            vehicle.validate()

    def test_tipo_veiculo_invalid_choice(self):
        """Testa escolha inválida de tipo de veículo"""
        data = self.valid_vehicle_data.copy()
        data['tipoVeiculo'] = 'invalid_choice'
        
        vehicle = Vehicle(**data)
        
        with self.assertRaises(ValidationError) as cm:
            vehicle.validate()
        
        self.assertIn('tipoVeiculo', str(cm.exception))

    def test_ano_fabricacao_range(self):
        """Testa validação de ano (lógica de negócio)"""
        data = self.valid_vehicle_data.copy()
        data['anoFabricacao'] = 1800  # Muito antigo
        
        vehicle = Vehicle(**data)
        
        # Ajustar baseado nas suas regras de negócio
        with self.assertRaises(ValidationError):
            vehicle.validate()

    def test_km_atual_negative(self):
        """Testa que valores negativos de km são rejeitados"""
        data = self.valid_vehicle_data.copy()
        data['kmAtual'] = -1000
        
        vehicle = Vehicle(**data)
        
        with self.assertRaises(ValidationError):
            vehicle.validate()

    def tearDown(self):
        """Limpa dados após cada teste"""
        Vehicle.objects.delete()