import { useState, useRef, useEffect } from 'react';
import { ModalContext } from '../contexts/modal.context';
import type {
  IHandleOpenModalProps,
  TModalContentID,
  TModalTypes
} from '../interfaces/modal.interface';
import type { IDefaultChildrenProp } from '@interfaces/default.interface';

const ModalProvider = ({ children }: IDefaultChildrenProp) => {
  const [modalType, setModalType] = useState<TModalTypes | null>(null);
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const [modalContentID, setModalContentID] = useState<TModalContentID>(null);
  const modalRef = useRef(null);

  useEffect(() => {
    const handleModalOutClick = (event: Event) => {
      if (modalRef.current === event.target) {
        handleCloseModal();
      }
    };
    window.addEventListener('click', handleModalOutClick);

    return () => {
      window.removeEventListener('click', handleModalOutClick);
    };
  }, []);

  const handleOpenModal = ({ modalType, id }: IHandleOpenModalProps) => {
    setIsOpen(true);
    setModalType(modalType);
    setModalContentID(id);
  };

  const handleCloseModal = () => {
    setIsOpen(false);
    setModalType(null);
    setModalContentID(null);
  };

  return (
    <ModalContext.Provider
      value={{
        modalType,
        modalRef,
        isOpen,
        handleOpenModal,
        handleCloseModal,
        modalContentID
      }}
    >
      {children}
    </ModalContext.Provider>
  );
};

export { ModalProvider };
