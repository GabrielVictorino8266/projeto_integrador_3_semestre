/* eslint-disable no-empty-pattern */
import { createContext } from "react";
import type { IModalContextProps } from "../interfaces";
import type { IHandleOpenModalProps } from "@interfaces/modal.interface";

const ModalContext = createContext<IModalContextProps>({
  modalType: null,
  isOpen: false,
  handleCloseModal: function (): void {},
  modalRef: { current: null },
  handleOpenModal: function ({}: IHandleOpenModalProps): void {},
  modalContentID: undefined,
});

export { ModalContext };
