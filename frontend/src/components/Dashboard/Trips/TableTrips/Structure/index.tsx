import { StyledTableRow } from "./styles";
import { useModal } from "@hooks/useModal";
import { StatusIcon } from "@components/Dashboard/Icons/StatusIcon";
import { GoToDriverEdit, IconButton } from "@styles/Buttons";
import { ActionIcon } from "@components/Dashboard/Icons/ActionIcon";
import type { TripStatus } from "@interfaces/trips.interface";

interface TripsItems {
    id: string;
    driverName: string; 
    vehicle: string;
    destination: string; 
    travelDate: string; 
    departureTime: string; 
    status: TripStatus;
    onDeleted?: () => void;
}

export const TripListItem = ({ id,driverName, vehicle, destination, travelDate, departureTime, status }: TripsItems) => {
    const { handleOpenModal } = useModal();

    const iconOption = status === "in_progress" ? "blueTrip" : status === "active" ? "blueTrip" : "yallow";

    return (
        <StyledTableRow>
            <td scope="row">{driverName}</td>
            <td>{vehicle}</td>
            <td>{destination}</td>
            <td>{travelDate}</td>
            <td>{departureTime}</td>
            <td>
                <button>
                    <StatusIcon option={iconOption} />
                </button>
            </td>
            <td>
                <GoToDriverEdit to={""}>
                    <ActionIcon type="edit" />
                </GoToDriverEdit>

                <IconButton
                    onClick={() =>
                        handleOpenModal({
                            modalType: "tripDeleteConfirmation",
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
