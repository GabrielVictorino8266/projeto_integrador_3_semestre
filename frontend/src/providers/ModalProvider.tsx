import { useState, useRef, useEffect } from "react";
import { ModalContext } from "../contexts/modal.context";
import { DriverRegisterModalContent } from "../components/Modal/ModalContents";
import type { JSX } from "@emotion/react/jsx-runtime";
import type { TModalTypes } from "../interfaces/modal.interface";
import type { IDefaultChildrenProp } from "@interfaces/default.interface";

const ModalProvider = ({ children }: IDefaultChildrenProp) => {
  const [modalType, setModalType] = useState<TModalTypes | null>(null);

  const MODALCOMPONENTS: Record<string, () => JSX.Element> = {
    driverRegister: DriverRegisterModalContent,
    // vehicleRegister: vehicleRegisterModalContent,
    // confirm: ConfirmModalContent,
  };

  const [isOpen, setIsOpen] = useState<boolean>(false);
  const modalRef = useRef(null);

  useEffect(() => {
    const handleModalOutClick = (event: Event) => {
      if (modalRef.current === event.target) {
        handleCloseModal();
      }
    };
    window.addEventListener("click", handleModalOutClick);

    return () => {
      window.removeEventListener("click", handleModalOutClick);
    };
  }, []);

  const handleOpenModal = (modalType: TModalTypes) => {
    setIsOpen(true);
    setModalType(modalType);
  };

  const handleCloseModal = () => {
    setIsOpen(false);
    setModalType(null);
  };

  return (
    <ModalContext.Provider
      value={{
        modalType,
        modalRef,
        isOpen,
        handleOpenModal,
        handleCloseModal,
        MODALCOMPONENTS,
      }}
    >
      {children}
    </ModalContext.Provider>
  );
};

export { ModalProvider };
