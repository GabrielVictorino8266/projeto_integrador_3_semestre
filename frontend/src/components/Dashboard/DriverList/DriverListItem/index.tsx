import { StyledTableRow } from "./styles";
import { FiTrash2 } from "react-icons/fi";
import { TbEdit } from "react-icons/tb";
import { FaCircle } from "react-icons/fa";
import { useModal } from "@hooks/useModal";
import { GoToDriverEdit } from "@styles/Buttons";

interface IDriverListItemProps {
  id: string;
  name: string;
  licenceType: string;
  cpf: string;
  performance: number;
  status: boolean;
}

const DriverListItem = ({
  id,
  name,
  performance,
  status,
  cpf,
  licenceType,
}: IDriverListItemProps) => {
  const { handleOpenModal } = useModal();

  return (
    <StyledTableRow>
      <td scope="row">{name}</td>
      <td>{cpf}</td>
      <td>{licenceType}</td>
      <td>{performance}</td>
      <td>
        <button>
          {status ? (
            <FaCircle className="iconButtonsEditDelete driverActive " />
          ) : (
            <FaCircle className="iconButtonsEditDelete driverInactive" />
          )}
        </button>
      </td>
      <td>
        <GoToDriverEdit to={`/dashboard/motorista/${id}`}>
          <TbEdit className="iconButtonsEditDelete editButton" />
        </GoToDriverEdit>
        <button
          onClick={() => {
            handleOpenModal({ modalType: "driverDeleteConfirmation", id });
          }}
        >
          <FiTrash2 className="iconButtonsEditDelete deleteButton" />
        </button>
      </td>
    </StyledTableRow>
  );
};

export { DriverListItem };
