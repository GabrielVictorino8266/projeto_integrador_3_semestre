import { Container, ContainerFilter, ContainerList, InputWrapper } from "./styles";
import { DashboardHeader } from "@components/Dashboard/Title";
import { GoToDriverRegister } from "@styles/Buttons";
import { CardWithRightBorder } from "@components/Dashboard/Cards";
import { StatusIcon } from "@components/Dashboard/Icons/StatusIcon";
import { DashboardTable } from "@components/Dashboard/Table";
import { ChartComponent, DoughnutChart } from "@components/Dashboard/Chart";
import { useVehicleStats } from "@hooks/Vehicle/useVehocleStats";
import { Pagination } from "@components/Pagination";
import { InputComponent } from "@components/Input";
import { SelectStatus } from "@components/SelectFilter";
import  vivi  from '@assets/Viagem.png'
import { useTripList } from "@hooks/Trip/useTripsList";
import { TripList } from "../TableTrips/Items";
import { StatusTripsDash } from "@utils/Selects/SelectTripsStatusDash";

export function TrisDashboard() {
    const { total, active, inactive, maintenance } = useVehicleStats();
    const { data, page, status, totalPages, destination , setPage, setStatus, setDestination } = useTripList();

    const datatochart = [
        { value: active, label: "Concuiídas" },
        { value: maintenance, label: "Programadas" },
        { value: inactive, label: "Em andamento" },
    ];

    const doughnutChartDriverData = {
        labels: datatochart.map((item) => item.label),
        datasets: [
            {
                label: "",
                data: datatochart.map((item) => item.value),
                backgroundColor: ["#28a745", "#ca8a29", "#17a2b8"],
                borderWidth: 2,
                borderRadius: 8,
                borderSkipped: false,
                cutout: "50%",
                radius: "100%",
            },
        ],
    };

    return (
        <div className="dashboardItems_container">
            <DashboardHeader>
                <p>
                    <img src={vivi} alt="" />
                    LISTAGEM DE VIAGENS
                </p>

                <GoToDriverRegister to={"/veiculos"}>CADASTRAR</GoToDriverRegister>
            </DashboardHeader>

            <Container>
                <section className="dashboard__details">
                    <div className="cards__container">
                        <CardWithRightBorder>
                            <div className="card__values">
                                <p className="card__text">Viagens agendadas</p>
                                <p className="card__number">{total}</p>
                            </div>
                        </CardWithRightBorder>

                        <CardWithRightBorder>
                            <div className="card__values">
                                <p className="card__text">
                                    <StatusIcon option="green" />
                                    <span className="card__number">{active}</span>
                                    Viagens concluídas
                                </p>
                            </div>

                            <div className="card__values">
                                <p className="card__text">
                                    <StatusIcon option="orange" />
                                    <span className="card__number">{maintenance}</span>
                                    Viagens programadas
                                </p>
                            </div>

                            <div className="card__values">
                                <p className="card__text">
                                    <StatusIcon option="blue" />
                                    <span className="card__number">{inactive}</span>
                                    Viagens em andamento
                                </p>
                            </div>
                        </CardWithRightBorder>

                        <CardWithRightBorder>
                            <p className="card__text">DISPONIBILIDADE</p>
                            <ChartComponent>
                                <DoughnutChart chartData={doughnutChartDriverData} />
                            </ChartComponent>
                        </CardWithRightBorder>
                    </div>

                    <ContainerFilter>
                        <InputWrapper>
                            <InputComponent
                                placeholder="FILTRAR POR DESTINO…"
                                value={destination}
                                onChange={(e) => setDestination(e.target.value)}
                                lupa
                            />
                        </InputWrapper>

                        <SelectStatus
                            onChange={(select) => setStatus("")}
                            value={status}
                            options={StatusTripsDash}
                        />
                    </ContainerFilter>

                    <ContainerList>
                        <DashboardTable
                            title="LISTA DE VEÍCULOS"
                            thTitles={["MOTORISTA","VEÍCULO","DESTINO", "DATA VIAGEM","HORÁRIO SAÍDA","STATUS", "AÇÕES" ]}
                        >
                            <TripList data={data} />
                        </DashboardTable>
                    </ContainerList>

                    <Pagination totalPages={totalPages} current={page} onChange={(p: number) => setPage(p)} />
                </section>
            </Container>
        </div>
    );
}
