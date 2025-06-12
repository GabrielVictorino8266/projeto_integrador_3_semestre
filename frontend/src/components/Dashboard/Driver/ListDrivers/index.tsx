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

const DriverDashboard = () => {
  const { driverActive, driverInactive, driverQuantity, getDriverList } =
    useDriver();

  useEffect(() => {
    getDriverList();
  }, []);

  return (
    <>
      <div className="dashboardItems_container">
        <DashboardHeader>
          <p>LISTAGEM DE MOTORISTAS</p>
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
                  <p className="card__number">{driverQuantity}</p>
                </div>
              </CardWithRightBorder>

              <CardWithRightBorder>
                <div className="card__values">
                  <p className="card__text">
                    <StatusIcon option={"blue"} />
                    Motoristas Ativos
                  </p>
                  <p className="card__number">{driverActive}</p>
                </div>

                <div className="card__values">
                  <p className="card__text">
                    <StatusIcon option={"red"} />
                    Motoristas Inativos
                  </p>
                  <p className="card__number">{driverInactive}</p>
                </div>
              </CardWithRightBorder>

              <CardWithRightBorder>
                <p>Gráfico</p>
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
