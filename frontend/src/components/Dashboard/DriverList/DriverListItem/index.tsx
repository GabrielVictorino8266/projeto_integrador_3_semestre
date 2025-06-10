import { StyledTableRow } from "./styles";
import { FiTrash2 } from "react-icons/fi";
import { TbEdit } from "react-icons/tb";
import { FaCircle } from "react-icons/fa";
import { useModal } from "@hooks/useModal";

interface IDriverListItemProps {
  id: string;
  name: string;
  licenceNumber: string;
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
  licenceNumber,
}: IDriverListItemProps) => {
  const { handleOpenModal } = useModal();

  return (
    <StyledTableRow>
      <td scope="row">{name}</td>
      <td>{cpf}</td>
      <td>{licenceNumber}</td>
      <td>{performance}</td>
      <td>
        <button>
          {status ? (
            <FaCircle className="icon driverActive " />
          ) : (
            <FaCircle className="icon driverInactive" />
          )}
        </button>
      </td>
      <td>
        <button
          onClick={() => {
            handleOpenModal({ modalType: "driverEdit", id });
          }}
        >
          <TbEdit className="icon editButton" />
        </button>
        <button
          onClick={() => {
            handleOpenModal({ modalType: "driverDeleteConfirmation", id });
          }}
        >
          <FiTrash2 className="icon deleteButton" />
        </button>
      </td>
    </StyledTableRow>
  );
};

export { DriverListItem };
