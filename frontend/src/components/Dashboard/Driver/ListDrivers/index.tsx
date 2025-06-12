import { Container } from "./styles";
import { DashboardHeader } from "@components/Dashboard/Title";
import { GoToDriverRegister } from "@styles/Buttons";
import { CardWithRightBorder } from "@components/Dashboard/Cards";
import { DriverList } from "@components/Dashboard/DriverList";
import { RegInput } from "@components/InputForm";
import { useDriver } from "@hooks/useDriver";
import { useEffect } from "react";

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
          <p>Motoristas</p>
          <GoToDriverRegister to={"/dashboard/cadastrar-motorista"}>
            CADASTRAR
          </GoToDriverRegister>
        </DashboardHeader>

        <Container>
          <section className="dashboard__details">
            <div className="cards__container">
              <CardWithRightBorder>
                <p>Total de motoristas</p>
                <p>{driverQuantity}</p>
              </CardWithRightBorder>

              <CardWithRightBorder>
                <p>Motoristas Ativos</p>
                <p>{driverActive}</p>
                <p>Motoristas Inativos</p>
                <p>{driverInactive}</p>
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

            <div>
              <div>
                <h2>Motoristas</h2>
              </div>
              <table>
                <thead>
                  <tr>
                    <th>Nome</th>
                    <th>CPF</th>
                    <th>Carteira</th>
                    <th>Aproveitamento</th>
                    <th>Status</th>
                    <th>Ações</th>
                  </tr>
                </thead>
                <DriverList />
              </table>
            </div>
          </section>
        </Container>
      </div>
    </>
  );
};

export { DriverDashboard };
