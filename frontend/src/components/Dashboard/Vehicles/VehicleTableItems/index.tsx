import { useVehicle } from "@hooks/useVehicle";
import { VehicleListItem } from "./Table";
import { StyledDriverList } from "./styles"; // pode renomear se quiser

export const VehicleList = () => {
  const { vehicleList } = useVehicle();

  return (
    <StyledDriverList>
      {vehicleList.map((v) => (
        <VehicleListItem
          key={v.id}
          id={v.id}
          licensePlate={v.licensePlate}
          vehicleType={v.vehicleType}
          manufacturingYear={v.manufacturingYear}
          brand={v.brand}
          status={v.status as "active" | "inactive"}
        />
      ))}
    </StyledDriverList>
  );
};
