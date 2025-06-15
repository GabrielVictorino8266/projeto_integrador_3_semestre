import { StyledTableRow } from "./styles";
import { useModal } from "@hooks/useModal";
import { StatusIcon } from "@components/Dashboard/Icons/StatusIcon";
import { GoToDriverEdit, IconButton } from "@styles/Buttons";
import { ActionIcon } from "@components/Dashboard/Icons/ActionIcon";

interface IVehicleListItemProps {
    id: string;
    licensePlate: string;
    vehicleType: string;
    manufacturingYear: number;
    brand: string;
    status: "active" | "inactive";
}

const VehicleListItem = ({
    id,
    licensePlate,
    vehicleType,
    manufacturingYear,
    brand,
    status,
}: IVehicleListItemProps) => {
    const { handleOpenModal } = useModal();

    return (
        <StyledTableRow>
            <td scope="row">{licensePlate}</td>
            <td>{vehicleType}</td>
            <td>{manufacturingYear}</td>
            <td>{brand}</td>
            <td>
                <button>
                    {status === "active" ? (
                        <StatusIcon option="blue" />
                    ) : (
                        <StatusIcon option="red" />
                    )}
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

export { VehicleListItem };
