import { Sidebar } from "@components/Sidebar";
import { Container, Main } from "./styles";
import { DashboardHeader } from "@components/Dashboard/Title";
import { Button } from "@styles/Buttons";
import { CardWithRightBorder } from "@components/Dashboard/Cards";
import { DriverList } from "@components/Dashboard/DriverList";
import { RegInput } from "@components/InputForm";
import { useDriver } from "@hooks/useDriver";
import { useModal } from "@hooks/useModal";
import { Modal } from "@components/Modal/ModalGeneric";
import { useEffect } from "react";

const DriverDashboard = () => {
  const { driverActive, driverInactive, driverQuantity, getDriverList } =
    useDriver();
  const { isOpen, modalType } = useModal();

  useEffect(() => {
    getDriverList();
  }, []);

  return (
    <>
      {isOpen && <Modal type={modalType} />}
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
      </Main>
    </>
  );
};

export { DriverDashboard };
