import { Route, Routes } from "react-router-dom";
import HomePage from "../pages/HomePage";
import { CadastroVeiculo } from "../pages/Cadastro/Veiculos";
import { Login } from "../pages/Login";
import { DriverRegister } from "../pages/Cadastro/Driver";
import { DriverDashboard } from "@pages/Dashboard/Driver";

const RoutesMain = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/motorista" element={<DriverRegister />} />
      <Route path="/dashboard/motoristas" element={<DriverDashboard />} />
      <Route path="/veiculos">
        <Route index element={<CadastroVeiculo />} />
        <Route path=":id" element={<CadastroVeiculo />} />
      </Route>
    </Routes>
  );
};

export default RoutesMain;
