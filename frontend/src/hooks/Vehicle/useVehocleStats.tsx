import { useEffect, useState } from 'react';
import { getVehicles } from '@services/Api/Vehicles/getVehicle';
import { toast } from 'react-toastify';
import { useDelayedSpinner } from '@hooks/useDelaydSpinner';

export const useVehicleStats = () => {
  const [total, setTotal] = useState(0);
  const [active, setActive] = useState(0);
  const [inactive, setInactive] = useState(0);
  const [maintenance, setMaintenance] = useState(0);
  const { showSpinner, startSpinner, stopSpinner } = useDelayedSpinner();

  async function fetchStats() {
    try {
      startSpinner();
      const [all, act, inac, main] = await Promise.all([
        getVehicles({ limit: 1 }),
        getVehicles({ status: 'active', limit: 1 }),
        getVehicles({ status: 'indisponivel', limit: 1 }),
        getVehicles({ status: 'maintenance', limit: 1 })
      ]);
      setTotal(all?.total ?? 0);
      setActive(act?.total ?? 0);
      setInactive(inac?.total ?? 0);
      setMaintenance(main?.total ?? 0);
    } catch (err) {
      toast.error('Erro ao carregar os status');
    } finally {
      stopSpinner();
    }
  }

  useEffect(() => {
    fetchStats();
  }, []);

  return {
    total,
    active,
    inactive,
    maintenance,
    LoadingStatus: showSpinner,
    refetch: fetchStats
  };
};
