export interface IModalChildrenProps {
  children: React.ReactNode;
}

export type TModalTypes =
  | 'driverDetails'
  | 'driverEdit'
  | 'driverDeleteConfirmation'
  | 'tripDetails'
  | 'tripEdit'
  | 'tripDeleteConfirmation'
  | 'vehicleDetails'
  | 'vehicleEdit'
  | 'vehicleDeleteConfirmation'
  | null;

export interface IGenericModalProps {
  type: TModalTypes | null;
}

export type TModalContentID = string | undefined | null;

export interface IHandleOpenModalProps {
  modalType: TModalTypes;
  id?: TModalContentID;
}

export interface IModalContextProps {
  modalType: TModalTypes;
  isOpen: boolean;
  handleOpenModal: ({ modalType, id }: IHandleOpenModalProps) => void;
  handleCloseModal: () => void;
  modalRef: React.RefObject<null>;
  modalContentID: string | null | undefined;
}
