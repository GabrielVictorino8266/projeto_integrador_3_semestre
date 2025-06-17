import { StyledTableRow } from "./styles";
import { useModal } from "@hooks/useModal";
import { GoToDriverEdit, IconButton } from "@styles/Buttons";
import { StatusIcon } from "@components/Dashboard/Icons/StatusIcon";
import { ActionIcon } from "@components/Dashboard/Icons/ActionIcon";

interface IDriverListItemProps {
    id: string;
    name: string;
    licenceType: string;
    cpf: string;
    performance: number;
    status: boolean;
}

const DriverListItem = ({ id, name, performance, status, cpf, licenceType }: IDriverListItemProps) => {
    const { handleOpenModal } = useModal();

    return (
        <StyledTableRow>
            <td scope="row">{name}</td>
            <td>{cpf}</td>
            <td>{licenceType}</td>
            <td>{performance}</td>
            <td>
                <button>{status ? <StatusIcon option={"blue"} /> : <StatusIcon option={"red"} />}</button>
            </td>
            <td>
                <GoToDriverEdit to={`/dashboard/motorista/${id}`}>
                    <ActionIcon type="edit" />
                </GoToDriverEdit>

                <IconButton
                    onClick={() => {
                        handleOpenModal({ modalType: "driverDeleteConfirmation", id });
                    }}
                >
                    <ActionIcon type="delete" />
                </IconButton>
            </td>
        </StyledTableRow>
    );
};

export { DriverListItem };
