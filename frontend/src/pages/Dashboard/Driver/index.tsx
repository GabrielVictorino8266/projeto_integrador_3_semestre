import { Sidebar } from "@components/Sidebar";
import { Container, Main } from "./styles";
import { DashboardHeader } from "@components/Dashboard/Title";
import { Button } from "@styles/Buttons";
import { CardWithRightBorder } from "@components/Dashboard/Cards";
import { DriverList } from "@components/Dashboard/DriverList";
import { RegInput } from "@components/InputForm";

const DriverDashboard = () => {
  return (
    <Main>
      <Sidebar />
      <div className="dashboardItems_container">
        <DashboardHeader>
          <p>Motoristas</p>
          <Button>Cadastrar</Button>
        </DashboardHeader>

        <Container>
          <section className="dashboard__details">
            <div className="cards__container">
              <CardWithRightBorder>
                <h3>Total de motoristas</h3>
                <p>30</p>
              </CardWithRightBorder>

              <CardWithRightBorder>
                <p>dados aqui</p>
              </CardWithRightBorder>

              <CardWithRightBorder>
                <p>dados aqui</p>
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
    </Main>
  );
};

export { DriverDashboard };
