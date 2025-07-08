import { Route, Routes, Navigate } from 'react-router-dom';
import HomePage from '../pages/HomePage';
import { CadastroVeiculo } from '../pages/Cadastro/Veiculos';
import { Login } from '../pages/Login';
import { DriverRegister } from '@components/Dashboard/Driver/CreateDriver';
import { DriverDashboard } from '@components/Dashboard/Driver/ListDrivers';
import { DriverUpdate } from '@components/Dashboard/Driver/UpdateDriver';
import DashboardLayout from '@pages/Dashboard/Layout';
import { VehicleDashboard } from '@components/Dashboard/Vehicles/listVehicles';
import { ProtectedRoutes } from './protectedRoutes';
import { TrisDashboard } from '@components/Dashboard/Trips/listTrips';
import { TripRegister } from '@components/Dashboard/Trips/RegisterTrip';
import { TripUpdate } from '@components/Dashboard/Trips/UpdateTrip';

const RoutesMain = () => (
  <Routes>
    <Route path='/login' element={<Login />} />
    <Route
      path='/'
      element={<Navigate to='/dashboard/cadastrar-motorista' replace />}
    />

    <Route element={<ProtectedRoutes />}>
      <Route path='/dashboard' element={<DashboardLayout />}>
        <Route index element={<HomePage />} />

        {/* motoristas */}
        <Route path='/dashboard/motoristas' element={<DriverDashboard />} />
        <Route
          path='/dashboard/cadastrar-motorista'
          element={<DriverRegister />}
        />
        <Route path='/dashboard/motorista/:id' element={<DriverUpdate />} />

        {/* veículos */}
        <Route path='/dashboard/veiculos' element={<VehicleDashboard />} />

        {/* viagens */}
        <Route path='/dashboard/viagens' element={<TrisDashboard />} />
        <Route path='/dashboard/cadastrar-viagem' element={<TripRegister />} />
        <Route path='/dashboard/viagem/:id' element={<TripUpdate />} />
      </Route>

      {/* cadastro / atualizar */}

      <Route path='/cadastrar-veiculo' element={<CadastroVeiculo />} />
      <Route path='/atualizar-veiculo/:id' element={<CadastroVeiculo />} />
    </Route>
  </Routes>
);

export default RoutesMain;
