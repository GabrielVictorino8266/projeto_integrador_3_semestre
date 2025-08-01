import {
  Container,
  ContainerFilter,
  ContainerList,
  InputWrapper
} from './styles';
import { DashboardHeader } from '@components/Dashboard/Title';
import { GoToDriverRegister } from '@styles/Buttons';
import { CardWithRightBorder } from '@components/Dashboard/Cards';
import { StatusIcon } from '@components/Dashboard/Icons/StatusIcon';
import { DashboardTable } from '@components/Dashboard/Table';
import { ChartComponent, DoughnutChart } from '@components/Dashboard/Chart';
import { VehicleList } from '@components/Dashboard/Vehicles/VehicleTableItems/';
import { useVehicleStats } from '@hooks/Vehicle/useVehocleStats';
import { useVehicleList } from '@hooks/Vehicle/useVehicleList';
import { Pagination } from '@components/Pagination';
import { InputComponent } from '@components/Input';
import { SelectStatus } from '@components/SelectFilter';
import { StatusOptions } from '@utils/Selects/SelectVehicleStatus';
import type { VehicleStatus } from '@interfaces/vehicles.interface';
import { FaBus } from 'react-icons/fa';
import { Spinner } from '@components/Spinner';

const VehicleDashboard = () => {
  const { total, active, inactive, maintenance, LoadingStatus } =
    useVehicleStats();
  const {
    data,
    page,
    plate,
    LoadingList,
    setPlate,
    setPage,
    setStatus,
    status,
    totalPages
  } = useVehicleList();

  const datatochart = [
    { value: active, label: 'Disponível' },
    { value: maintenance, label: 'Em manutenção' },
    { value: inactive, label: 'Indisponível' }
  ];

  const doughnutChartDriverData = {
    labels: datatochart.map((item) => item.label),
    datasets: [
      {
        label: '',
        data: datatochart.map((item) => item.value),
        backgroundColor: ['#0073e6', '#ca8a29', '#b31010'],
        borderWidth: 2,
        borderRadius: 8,
        borderSkipped: false,
        cutout: '50%',
        radius: '100%'
      }
    ]
  };

  return (
    <div className='dashboardItems_container'>
      <DashboardHeader>
        <p>
          <FaBus />
          LISTAGEM DE VEÍCULOS
        </p>

        <GoToDriverRegister to={'/cadastrar-veiculo'}>
          CADASTRAR
        </GoToDriverRegister>
      </DashboardHeader>

      <Container>
        <section className='dashboard__details'>
          {LoadingStatus ? (
            <Spinner />
          ) : (
            <div className='cards__container'>
              <CardWithRightBorder>
                <div className='card__values'>
                  <p className='card__text'>Total de veículos</p>
                  <p className='card__number'>{total}</p>
                </div>
              </CardWithRightBorder>

              <CardWithRightBorder>
                <div className='card__values'>
                  <p className='card__text'>
                    <StatusIcon option='blue' />
                    <span className='card__number'>{active}</span>
                    Veículos Ativos
                  </p>
                </div>

                <div className='card__values'>
                  <p className='card__text'>
                    <StatusIcon option='orange' />
                    <span className='card__number'>{maintenance}</span>
                    Em manutenção
                  </p>
                </div>

                <div className='card__values'>
                  <p className='card__text'>
                    <StatusIcon option='red' />
                    <span className='card__number'>{inactive}</span>
                    Veículos Inativos
                  </p>
                </div>
              </CardWithRightBorder>

              <CardWithRightBorder>
                <p className='card__text'>DISPONIBILIDADE</p>
                <ChartComponent>
                  <DoughnutChart chartData={doughnutChartDriverData} />
                </ChartComponent>
              </CardWithRightBorder>
            </div>
          )}

          <ContainerFilter>
            <InputWrapper>
              <InputComponent
                placeholder='PESQUISAR POR PLACA..'
                lupa
                onChange={(e) => setPlate(e.target.value)}
                backgoround='#ffffff'
                value={plate}
                autoComplete='off'
              />
            </InputWrapper>

            <SelectStatus
              onChange={(val) => setStatus((val as VehicleStatus) || null)}
              value={status}
              options={StatusOptions}
            />
          </ContainerFilter>

          <ContainerList>
            {LoadingList ? (
              <Spinner />
            ) : (
              <DashboardTable
                title='LISTA DE VEÍCULOS'
                thTitles={['PLACA', 'TIPO', 'ANO', 'MARCA', 'STATUS', 'AÇÕES']}
              >
                <VehicleList data={data} />
              </DashboardTable>
            )}
          </ContainerList>

          <Pagination
            totalPages={totalPages}
            current={page}
            onChange={(p: number) => setPage(p)}
          />
        </section>
      </Container>
    </div>
  );
};

export { VehicleDashboard };
