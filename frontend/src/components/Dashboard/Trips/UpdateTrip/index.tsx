import { RegInput } from '@components/InputForm';
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm, type SubmitHandler } from 'react-hook-form';
import { RegisterPageGeneric } from '@components/RegisterForm';
import { DarkBlueButton } from '@styles/Buttons';
import { SelectInputForm } from '@components/Select';
import { useDriver } from '@hooks/useDriver';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { dateMask, hourMask } from '@utils/reserve';
import { ContainerInputs } from '@pages/Cadastro/Veiculos/styles';
import { GrMapLocation } from 'react-icons/gr';
import { useTrip } from '@hooks/useTrip';
import { tripCreateFormSchema } from '@schemas/tripCreateSchema';
import { TripStatus } from '@utils/Selects/tripStatus';
import type { IVehicle } from '@interfaces/vehicles.interface';
import { api } from '@services/api';
import type {
  ICreateTripRequest,
  ITripFormData
} from '@interfaces/trips.interface';

const TripUpdate = () => {
  interface ISelectOptions {
    value: string;
    label: string;
  }

  const [tripDateValue, setTripDateValue] = useState('');
  const [tripHourValue, setTripHourValue] = useState('');
  const [vehicleListData, setVehicleListData] = useState<Array<ISelectOptions>>(
    []
  );
  const [isLoading, setIsloading] = useState(true);

  const { getTripByID, tripUnderEdition, setTripUnderEdition, updateTrip } =
    useTrip();
  const { getDriverList, driverList } = useDriver();

  const { id } = useParams();

  const driverListSelect: Array<ISelectOptions> = driverList.map((driver) => ({
    value: driver.id,
    label: driver.name
  }));

  const vehiclesList = async () => {
    try {
      const res = await api.get('/vehicles/');

      if (res.status === 200) {
        const vehicleListSelect: Array<ISelectOptions> = res.data.items.map(
          (vehicle: IVehicle) => ({
            value: vehicle.id,
            label: vehicle.licensePlate
          })
        );
        setVehicleListData(vehicleListSelect);
      }
    } catch (error) {
      console.log(error);
    } finally {
      setIsloading(false);
    }
  };

  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors }
  } = useForm({
    resolver: zodResolver(tripCreateFormSchema)
  });

  useEffect(() => {
    if (id) {
      getTripByID(id);
    }
    getDriverList({ isActive: 'true' });
    return () => setTripUnderEdition(null);
  }, [id]);

  console.log(tripDateValue);

  useEffect(() => {
    if (tripUnderEdition) {
      setValue('destination', tripUnderEdition.destination);
      setValue('origin', tripUnderEdition.origin);
      setValue('initialKm', tripUnderEdition.initialKm);
      setValue('vehicleId', tripUnderEdition.vehicleId);
      setValue('status', tripUnderEdition.status);

      const splittedField = tripUnderEdition?.startDateTime
        .replace(/Z/g, '')
        .split('T');

      const dateReversed = splittedField[0].split('-').reverse().join('');
      setTripDateValue(dateReversed);

      setValue('tripDate', dateMask(tripDateValue));
      setValue('tripHour', hourMask(splittedField![1]));
      setValue('driverId', tripUnderEdition.driverId);
    }
  }, [tripUnderEdition, setValue]);

  const submitTrip: SubmitHandler<ITripFormData> = async (
    registerForm: ITripFormData
  ) => {
    const { tripDate, tripHour, ...rest } = registerForm;

    const newTripTreatedData: ICreateTripRequest = {
      ...rest,
      startDateTime: `${tripDate}T${tripHour}`
    };
    updateTrip(id!, newTripTreatedData);
  };

  useEffect(() => {
    if (isLoading === true) {
      getDriverList({ isActive: 'true' });
      vehiclesList();
    }
  }, [isLoading]);

  return (
    <RegisterPageGeneric icon={<GrMapLocation />} title={'EDITAR VIAGEM'}>
      <form onSubmit={handleSubmit(submitTrip)}>
        <ContainerInputs>
          <SelectInputForm
            optionsArray={driverListSelect}
            label={'Motorista'}
            {...register('driverId')}
            error={errors.driverId}
          />
          <SelectInputForm
            optionsArray={vehicleListData}
            id={'vehicle'}
            label={'Veículo'}
            {...register('vehicleId')}
            error={errors.vehicleId}
          />
          <RegInput
            type={'number'}
            placeholder={'ex: 10000'}
            id={'initialKM'}
            label={'Km do veículo'}
            {...register('initialKm', { valueAsNumber: true })}
            error={errors.initialKm}
          />
          <RegInput
            type={'text'}
            placeholder={'DD/MM/AAAA'}
            id={'tripDate'}
            label={'Data da viagem'}
            {...register('tripDate')}
            error={errors.tripDate}
            value={tripDateValue}
            onChange={(event) => {
              setTripDateValue(dateMask(event.target.value));
            }}
          />
          <RegInput
            type={'text'}
            placeholder={'HH:MM'}
            id={'tripHour'}
            label={'Horário'}
            {...register('tripHour')}
            error={errors.tripHour}
            value={tripHourValue}
            onChange={(event) => {
              setTripHourValue(hourMask(event.target.value));
            }}
          />
          <RegInput
            type={'text'}
            placeholder={'Ex: Leme'}
            id={'origin'}
            label={'Origem'}
            {...register('origin')}
            error={errors.origin}
          />
          <RegInput
            type={'text'}
            placeholder={'Ex: São Paulo'}
            id={'destination'}
            label={'Destino'}
            {...register('destination')}
            error={errors.destination}
          />
          <SelectInputForm
            optionsArray={TripStatus}
            id={'tripStatus'}
            label={'Status'}
            {...register('status')}
            error={errors.status}
          />
        </ContainerInputs>
        <div className='form__sendButton'>
          <DarkBlueButton>ENVIAR</DarkBlueButton>
        </div>
      </form>
    </RegisterPageGeneric>
  );
};

export { TripUpdate };
