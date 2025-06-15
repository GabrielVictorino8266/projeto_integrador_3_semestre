// @components/Dashboard/Vehicles/VehicleTableItems/index.tsx
import type { IVehicle } from "@interfaces/vehicles.interface";
import { VehicleListItem } from "./Table";
import { StyledDriverList } from "./styles";

interface Props {
  data: IVehicle[];
}

export const VehicleList = ({ data }: Props) => (
  <StyledDriverList>
    {data.map((v) => (
      <VehicleListItem
        key={v.id}
        id={v.id}
        licensePlate={v.licensePlate}
        vehicleType={v.vehicleType}
        manufacturingYear={v.manufacturingYear}
        brand={v.brand}
        status={v.status}
      />
    ))}
  </StyledDriverList>
);
