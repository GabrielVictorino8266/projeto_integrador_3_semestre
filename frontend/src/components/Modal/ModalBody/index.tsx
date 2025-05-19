import { useContext } from "react";
import type { IDefaultProviderProps } from "../../../interfaces";
import { ModalContext } from "../../../contexts/modal.context";
import { ModalBodyStyled } from "./style";

const ModalBody = ({ children }: IDefaultProviderProps) => {
  const { handleCloseModal } = useContext(ModalContext);
  return (
    <>
      <ModalBodyStyled className="modal__body">
        <h2>ModalBody</h2>
        <button
          onClick={() => {
            handleCloseModal();
          }}
        >
          Fechar
        </button>
        {children}
      </ModalBodyStyled>
    </>
  );
};

export { ModalBody };
