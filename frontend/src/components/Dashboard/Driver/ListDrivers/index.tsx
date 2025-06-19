import { Container } from "./styles";
import { DashboardHeader } from "@components/Dashboard/Title";
import { GoToDriverRegister } from "@styles/Buttons";
import { CardWithRightBorder } from "@components/Dashboard/Cards";
import { DriverList } from "@components/Dashboard/DriverList";
import { RegInput } from "@components/InputForm";
import { useDriver } from "@hooks/useDriver";
import { useEffect } from "react";
import { StatusIcon } from "@components/Dashboard/Icons/StatusIcon";
import { DashboardTable } from "@components/Dashboard/Table";
import { ChartComponent, DoughnutChart } from "@components/Dashboard/Chart";
import { TbSteeringWheelFilled } from "react-icons/tb";

const DriverDashboard = () => {
  const { driverActive, driverInactive, driverQuantity, getDriverList } =
    useDriver();

  useEffect(() => {
    getDriverList();
  }, []);

  const datatochart = [
    {
      value: driverActive,
      label: "Ativos",
    },
    { value: driverInactive, label: "Inativos" },
  ];

  const doughnutChartDriverData = {
    labels: datatochart.map((item) => item.label),
    datasets: [
      {
        label: "",
        data: datatochart.map((item) => item.value),
        backgroundColor: ["#0073e6", "#b31010"],
        borderWidth: 2,
        borderRadius: 8,
        borderSkipped: false,
        cutout: "50%",
        radius: "100%",
      },
    ],
  };

  return (
    <>
      <div className="dashboardItems_container">
        <DashboardHeader>
          <p>
            <TbSteeringWheelFilled />
            LISTAGEM DE MOTORISTAS
          </p>
          <GoToDriverRegister to={"/dashboard/cadastrar-motorista"}>
            CADASTRAR
          </GoToDriverRegister>
        </DashboardHeader>

        <Container>
          <section className="dashboard__details">
            <div className="cards__container">
              <CardWithRightBorder>
                <div className="card__values">
                  <p className="card__text">Total de motoristas</p>
                  <span className="card__number">{driverQuantity}</span>
                </div>
              </CardWithRightBorder>

              <CardWithRightBorder>
                <div className="card__values">
                  <p className="card__text">
                    <StatusIcon option={"blue"} />
                    <span className="card__number">{driverActive}</span>
                    Motoristas Ativos
                  </p>
                </div>

                <div className="card__values">
                  <p className="card__text">
                    <StatusIcon option={"red"} />
                    <span className="card__number">{driverInactive}</span>
                    Motoristas Inativos
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

            <div>
              <RegInput
                id="driverSearch"
                type="text"
                placeholder="Pesquisar"
                label={""}
              />
            </div>

            <DashboardTable
              title="LISTA DE MOTORISTAS"
              thTitles={["NOME", "CPF", "CNH", "AVALIAÇÃO", "STATUS", "AÇÕES"]}
            >
              <DriverList />
            </DashboardTable>
          </section>
        </Container>
      </div>
    </>
  );
};

export { DriverDashboard };
