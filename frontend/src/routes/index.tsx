import { Route, Routes } from "react-router-dom";
import Dashboard from "../pages/Dashboard";
import HomePage from "../pages/HomePage";
import { CadastroVeiculo } from "../pages/Cadastro/Veiculos";
import { Login } from "../pages/Login";
import { DriverRegister } from "../pages/Cadastro/Driver";
import { TripRegister } from "@pages/Cadastro/Trips";

const RoutesMain = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/veiculos" element={<CadastroVeiculo />} />
      <Route path="/motorista" element={<DriverRegister />} />
      <Route path="/viagens" element={<TripRegister />} />
    </Routes>
  );
};

export default RoutesMain;
