import { useContext } from 'react';
import { DriverContext } from '@contexts/driver.context';

const useDriver = () => {
  const driverContext = useContext(DriverContext);
  return driverContext;
};

export { useDriver };
