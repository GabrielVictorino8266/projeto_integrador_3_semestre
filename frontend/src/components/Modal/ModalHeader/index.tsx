import { ModalHeaderStyled } from "./style";
import { useModal } from "../../../hooks";

interface IModalTitle {
  modalTitle: string;
}

const ModalHeader = ({ modalTitle }: IModalTitle) => {
  const { handleCloseModal } = useModal();

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
