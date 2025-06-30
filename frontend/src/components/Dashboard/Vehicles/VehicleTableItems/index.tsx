// @components/Dashboard/Vehicles/VehicleTableItems/index.tsx
import type { IVehicle } from '@interfaces/vehicles.interface';
import { VehicleListItem } from './Table';
import { StyledDriverList } from './styles';
import { MaskLicensePlate } from '@utils/Mask/MaskLicensePlate';

interface Props {
  data: IVehicle[];
}

export const VehicleList = ({ data }: Props) => {
  const plateMask = new MaskLicensePlate();

  return (
    <StyledDriverList>
      {data.map((v) => (
        <VehicleListItem
          key={v.id}
          id={v.id}
          licensePlate={plateMask.mask(v.licensePlate)}
          vehicleType={v.vehicleType
            .replace('onibus', 'ônibus')
            .replace('caminhao', 'caminhão')
            .toUpperCase()}
          manufacturingYear={v.manufacturingYear}
          brand={v.brand}
          status={v.status}
        />
      ))}
    </StyledDriverList>
  );
};
