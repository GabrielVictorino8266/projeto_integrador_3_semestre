import { useDriver } from '@hooks/useDriver';
import { DriverListItem } from './DriverListItem';
import { StyledDriverList } from './styles';

const DriverList = () => {
  const { driverList } = useDriver();

  const driversElements = driverList.map((driver) => {
    const { id, name, cpf, performance, isActive, licenseType } = driver;

    return (
      <DriverListItem
        key={id}
        id={id}
        name={name}
        cpf={cpf}
        licenceType={licenseType}
        performance={performance}
        status={isActive}
      />
    );
  });

  return <StyledDriverList>{driversElements}</StyledDriverList>;
};

export { DriverList };
