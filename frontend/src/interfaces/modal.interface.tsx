import type { JSX } from "react";

export interface IModalChildrenProps {
  children: React.ReactNode;
}

export type TModalTypes = "driverRegister" | null;

export interface IModalContextProps {
  modalType: TModalTypes;
  isOpen: boolean;
  handleOpenModal: (modalType: TModalTypes) => void;
  handleCloseModal: () => void;
  modalRef: React.RefObject<null>;
  MODALCOMPONENTS: Record<Exclude<TModalTypes, null>, () => JSX.Element>;
}
