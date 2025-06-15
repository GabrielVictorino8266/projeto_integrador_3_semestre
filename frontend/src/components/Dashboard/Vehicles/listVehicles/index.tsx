import { Container } from "./styles";
import { DashboardHeader } from "@components/Dashboard/Title";
import { GoToDriverRegister } from "@styles/Buttons";
import { CardWithRightBorder } from "@components/Dashboard/Cards";
import { RegInput } from "@components/InputForm";
import { useVehicle } from "@hooks/useVehicle";
import { useEffect } from "react";
import { StatusIcon } from "@components/Dashboard/Icons/StatusIcon";
import { DashboardTable } from "@components/Dashboard/Table";
import { ChartComponent, DoughnutChart } from "@components/Dashboard/Chart";
import {VehicleList} from "@components/Dashboard/Vehicles/VehicleTableItems/"

const VehicleDashboard = () => {
    const { vehicleActive, vehicleInactive, vehicleQuantity, getVehicleList } =
        useVehicle();

    useEffect(() => {
        getVehicleList();
    }, []);

    const datatochart = [
        { value: vehicleActive, label: "Disponível" },
        { value: vehicleInactive, label: "Em manutenção" },
        { value: vehicleInactive, label: "Indisponível" },
    ];

    const doughnutChartDriverData = {
        labels: datatochart.map((item) => item.label),
        datasets: [
            {
                label: "",
                data: datatochart.map((item) => item.value),
                backgroundColor: ["#0073e6", "#ca8a29", "#b31010"],
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
                <p>LISTAGEM DE VEÍCULOS</p>
                <GoToDriverRegister to={"/veiculos"}>
                    CADASTRAR
                </GoToDriverRegister>
            </DashboardHeader>

            <Container>
                <section className="dashboard__details">
                    <div className="cards__container">
                        <CardWithRightBorder>
                            <div className="card__values">
                                <p className="card__text">Total de veículos</p>
                                <p className="card__number">
                                    {vehicleQuantity}
                                </p>
                            </div>
                        </CardWithRightBorder>

                        <CardWithRightBorder>
                            <div className="card__values">
                                <p className="card__text">
                                    <StatusIcon option={"blue"} />
                                    Veículos Ativos
                                </p>
                                <p className="card__number">{vehicleActive}</p>
                            </div>

                            <div className="card__values">
                                <p className="card__text">
                                    <StatusIcon option={"orange"} />
                                    Em manutenção
                                </p>
                                <p className="card__number">
                                    {vehicleInactive}
                                </p>
                            </div>

                            <div className="card__values">
                                <p className="card__text">
                                    <StatusIcon option={"red"} />
                                    Veículos Inativos
                                </p>
                                <p className="card__number">
                                    {vehicleInactive}
                                </p>
                            </div>
                        </CardWithRightBorder>

                        <CardWithRightBorder>
                            <p className="card__text">DISPONIBILIDADE</p>
                            <ChartComponent>
                                <DoughnutChart
                                    chartData={doughnutChartDriverData}
                                />
                            </ChartComponent>
                        </CardWithRightBorder>
                    </div>

                    <div>
                        <RegInput
                            id="vehicleSearch"
                            type="text"
                            placeholder="Pesquisar"
                            label={""}
                        />
                    </div>

                    <DashboardTable
                        title="LISTA DE VEÍCULOS"
                        thTitles={[
                            "PLACA",
                            "TIPO",
                            "ANO",
                            "MARCA",
                            "STATUS",
                            "AÇÕES",
                        ]}
                    >
                        <VehicleList />
                    </DashboardTable>
                </section>
            </Container>
        </div>
    );
};

export { VehicleDashboard };
