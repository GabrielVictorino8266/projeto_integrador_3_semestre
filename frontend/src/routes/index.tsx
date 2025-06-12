import { Route, Routes } from "react-router-dom";
import HomePage from "../pages/HomePage";
import { CadastroVeiculo } from "../pages/Cadastro/Veiculos";
import { Login } from "../pages/Login";
import DashboardLayout from "@pages/Dashboard/Layout";
import { DriverDashboard } from "@components/Dashboard/Driver/ListDrivers";
import { DriverRegister } from "@pages/Cadastro/Driver";
import { DriverUpdate } from "@components/Dashboard/Driver/UpdateDriver";

const RoutesMain = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<DashboardLayout />}>
        <Route index element={<HomePage />} />
        <Route path="/dashboard/motoristas" element={<DriverDashboard />} />
        <Route
          path="/dashboard/cadastrar-motorista"
          element={<DriverRegister />}
        />
        <Route path="/dashboard/motorista/:id" element={<DriverUpdate />} />
      </Route>
      <Route path="/veiculos">
        <Route index element={<CadastroVeiculo />} />
        <Route path=":id" element={<CadastroVeiculo />} />
      </Route>
    </Routes>
  );
};

export default RoutesMain;
