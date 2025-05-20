import { useContext } from "react";
import { ModalHeaderStyled } from "./style";
import { ModalContext } from "../../../contexts/modal.context";

interface IModalTitle {
  modalTitle: string;
}
const ModalHeader = ({ modalTitle }: IModalTitle) => {
  const { handleCloseModal } = useContext(ModalContext);

  return (
    <ModalHeaderStyled>
      <p>{modalTitle}</p>
      <button
        onClick={() => {
          handleCloseModal();
        }}
      >
        X
      </button>
    </ModalHeaderStyled>
  );
};

export { ModalHeader };
