import { zodResolver } from '@hookform/resolvers/zod';
import { useNavigate, useParams } from 'react-router-dom';
import { useForm } from 'react-hook-form';
// Componente
import { Sidebar } from '@components/Sidebar';
import { RegisterPageGeneric } from '@components/RegisterForm';
import { SelectInputForm } from '@components/Select';
import { InputComponent } from '@components/Input';
// Utils
import { veiculos } from '@utils/Selects/TipoVeiculos';
import { status } from '@utils/Selects/StatusVeiculo';
// hooks
import { useFetchVeiculos } from '@hooks/useFetchVeiculos/index';
// Schemas
import { schemaCadVeiculo, type DataProps } from '@schemas/CadsVeiculos';
// Service
import { VehiclesRegistration } from '@services/Api/Vehicles/VehiclesRegistration';
// Styles
import { ButtonWrapper, Container, ContainerInputs } from './styles';
import { FaBus } from 'react-icons/fa';
import { DarkBlueButton } from '@styles/Buttons';

export function CadastroVeiculo() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const currentYear = new Date().getFullYear();

  const {
    register,
    handleSubmit,
    formState: { errors },
    reset
  } = useForm<DataProps>({
    resolver: zodResolver(schemaCadVeiculo)
  });

  const { loading } = useFetchVeiculos(id, reset);

  if (loading) return <p>Carregando...</p>;

  const Submit = async (data: DataProps) => {
    const sucess = await VehiclesRegistration(data, id);
    if (sucess) {
      reset();
    }
    if (id && sucess) {
      setTimeout(() => navigate('/dashboard/veiculos'), 900);
    }
  };

  return (
    <Container>
      <Sidebar />
      <RegisterPageGeneric icon={<FaBus />} title='Cadastro de veículo'>
        <form onSubmit={handleSubmit(Submit)}>
          <ContainerInputs>
            <InputComponent
              label='Placa'
              {...register('licensePlate')}
              placeholder='ABC-1234'
              mask='licensePlate'
              maxLength={8}
              errorMessage={errors.licensePlate?.message}
            />
            <InputComponent
              label='Marca'
              {...register('brand')}
              placeholder='Marca'
              errorMessage={errors.brand?.message}
            />
            <InputComponent
              label='Número'
              {...register('vehicleNumber')}
              placeholder='Número do veículo'
              mask='km'
              errorMessage={errors.vehicleNumber?.message}
            />
            <InputComponent
              label='Ano do veículo'
              {...register('manufacturingYear')}
              placeholder={`Ex: ${currentYear}`}
              maxLength={4}
              errorMessage={errors.manufacturingYear?.message}
            />
            <InputComponent
              label='KM do veículo'
              {...register('currentKm')}
              placeholder='Km do veículo'
              mask='km'
              errorMessage={errors.currentKm?.message}
            />
            <InputComponent
              label='Limte de KM para aviso'
              {...register('warningKmLimit')}
              placeholder='KM limite'
              mask='km'
              errorMessage={errors.warningKmLimit?.message}
            />
            <SelectInputForm
              label='Tipo de veículo'
              optionsArray={veiculos}
              {...register('vehicleType')}
              error={errors.vehicleType}
            />
            <SelectInputForm
              label='Status'
              optionsArray={status}
              {...register('status')}
              error={errors.status}
            />
          </ContainerInputs>

          <ButtonWrapper>
            <DarkBlueButton type='submit'>
              {id ? 'Atualizar' : 'Cadastrar'}
            </DarkBlueButton>
          </ButtonWrapper>
        </form>
      </RegisterPageGeneric>
    </Container>
  );
}
