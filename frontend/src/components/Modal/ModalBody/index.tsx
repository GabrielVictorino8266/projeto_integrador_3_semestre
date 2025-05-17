import { useContext } from "react";
import type { IDefaultProviderProps } from "../../../interfaces";
import { ModalContext } from "../../../contexts/modal.context";

const ModalBody = ({ children }: IDefaultProviderProps) => {
  const { handleCloseModal } = useContext(ModalContext);
  return (
    <>
      <h2>ModalBody</h2>
      <button
        onClick={() => {
          handleCloseModal();
        }}
      >
        Fechar
      </button>
      {children}
    </>
  );
};

export { ModalBody };
