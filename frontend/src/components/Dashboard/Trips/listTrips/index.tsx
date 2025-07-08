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
import { Pagination } from '@components/Pagination';
import { InputComponent } from '@components/Input';
import { SelectStatus } from '@components/SelectFilter';
import vivi from '@assets/Viagem.png';
import { useTripList } from '@hooks/Trip/useTripsList';
import { TripList } from '../TableTrips/Items';
import { StatusTripsDash } from '@utils/Selects/SelectTripsStatusDash';
import { useTripsStats } from '@hooks/Trip/useTripsStats';
import { Spinner } from '@components/Spinner';

export function TrisDashboard() {
  const { total, completed, inProgress, scheduled, LoadingVehiclStatus } =
    useTripsStats();
  const {
    data,
    page,
    status,
    totalPages,
    destination,
    LoadingVehiclList,
    setPage,
    setStatus,
    setDestination
  } = useTripList();

  const datatochart = [
    { value: completed, label: 'Concluídas' },
    { value: scheduled, label: 'Programadas' },
    { value: inProgress, label: 'Em andamento' }
  ];

  const doughnutChartDriverData = {
    labels: datatochart.map((item) => item.label),
    datasets: [
      {
        label: '',
        data: datatochart.map((item) => item.value),
        backgroundColor: ['#15670a', '#0073e6', '#b31010'],
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
          <img src={vivi} alt='' />
          LISTAGEM DE VIAGENS
        </p>

        <GoToDriverRegister to={'/dashboard/cadastrar-viagem'}>
          CADASTRAR
        </GoToDriverRegister>
      </DashboardHeader>

      <Container>
        <section className='dashboard__details'>
          {LoadingVehiclStatus ? (
            <Spinner />
          ) : (
            <div className='cards__container'>
              <CardWithRightBorder>
                <div className='card__values'>
                  <p className='card__text'>Viagens agendadas</p>
                  <p className='card__number'>{total}</p>
                </div>
              </CardWithRightBorder>

              <CardWithRightBorder>
                <div className='card__values'>
                  <p className='card__text'>
                    <StatusIcon option='green' />
                    <span className='card__number'>{completed}</span>
                    Viagens concluídas
                  </p>
                </div>

                <div className='card__values'>
                  <p className='card__text'>
                    <StatusIcon option='blue' />
                    <span className='card__number'>{scheduled}</span>
                    Viagens programadas
                  </p>
                </div>

                <div className='card__values'>
                  <p className='card__text'>
                    <StatusIcon option='red' />
                    <span className='card__number'>{inProgress}</span>
                    Viagens em andamento
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
                placeholder='FILTRAR POR DESTINO…'
                value={destination}
                onChange={(e) => setDestination(e.target.value)}
                lupa
                backgoround='#ffffff'
              />
            </InputWrapper>

            <SelectStatus
              onChange={(select) => setStatus(select ?? '')}
              value={status}
              options={StatusTripsDash}
            />
          </ContainerFilter>

          <ContainerList>
            {LoadingVehiclList ? (
              <Spinner />
            ) : (
              <DashboardTable
                title='LISTA DE VEÍCULOS'
                thTitles={[
                  'MOTORISTA',
                  'VEÍCULO',
                  'DESTINO',
                  'DATA VIAGEM',
                  'HORÁRIO SAÍDA',
                  'STATUS',
                  'AÇÕES'
                ]}
              >
                <TripList data={data} />
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
}
