import { StyledTableRow } from "./styles";
import { useModal } from "@hooks/useModal";
import { StatusIcon } from "@components/Dashboard/Icons/StatusIcon";
import { GoToDriverEdit, IconButton } from "@styles/Buttons";
import { ActionIcon } from "@components/Dashboard/Icons/ActionIcon";
import type { VehicleStatus } from "@interfaces/vehicles.interface";   // ← novo

interface IVehicleListItemProps {
  id: string;
  licensePlate: string;
  vehicleType: string;
  manufacturingYear: number;
  brand: string;
  status: VehicleStatus;       
}

export const VehicleListItem = ({
  id,
  licensePlate,
  vehicleType,
  manufacturingYear,
  brand,
  status,
}: IVehicleListItemProps) => {
  const { handleOpenModal } = useModal();

  const iconOption =
    status === "active"
      ? "blue"
      : status === "maintenance"
      ? "orange"
      : "red"; 

  return (
    <StyledTableRow>
      <td scope="row">{licensePlate}</td>
      <td>{vehicleType}</td>
      <td>{manufacturingYear}</td>
      <td>{brand}</td>
      <td>
        <button>
          <StatusIcon option={iconOption} />
        </button>
      </td>
      <td>
        <GoToDriverEdit to={`/veiculos/${id}`}>
          <ActionIcon type="edit" />
        </GoToDriverEdit>

        <IconButton
          onClick={() =>
            handleOpenModal({
              modalType: "vehicleDeleteConfirmation",
              id,
            })
          }
        >
          <ActionIcon type="delete" />
        </IconButton>
      </td>
    </StyledTableRow>
  );
};
