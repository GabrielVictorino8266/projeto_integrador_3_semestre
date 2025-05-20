import { createContext } from "react";
import type { IModalContextProps } from "../interfaces";

const ModalContext = createContext<IModalContextProps>({
  isOpen: false,
  handleOpenModal: () => {},
  handleCloseModal: () => {},
  modalRef: { current: null },
  MODALCOMPONENTS: {
    driverRegister: () => <></>,
  },
  modalType: null,
});

export { ModalContext };
