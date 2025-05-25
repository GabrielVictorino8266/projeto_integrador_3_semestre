import { Route, Routes } from "react-router-dom";
import Dashboard from "../pages/Dashboard";
import HomePage from "../pages/HomePage";
import { CadastroVeiculo } from "../pages/Cadastro/Veiculos";
import { Login } from "../pages/Login";



const RoutesMain = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="veiculos" element={<CadastroVeiculo />} />
    </Routes>
  );
};

export default RoutesMain;
