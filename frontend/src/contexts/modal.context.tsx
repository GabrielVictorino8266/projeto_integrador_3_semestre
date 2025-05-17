import { createContext, useEffect, useRef, useState } from "react";
import type { IDefaultProviderProps, IModalContextProps } from "../interfaces";

const ModalContext = createContext({} as IModalContextProps);

const ModalProvider = ({ children }: IDefaultProviderProps) => {
  const [isOpen, setIsOpen] = useState(false);
  const refference = useRef(null);

  useEffect(() => {
    const handleModalOutClick = (event: Event) => {
      if (refference.current === event.target) {
        handleOpenModal();
      }
    };
    window.addEventListener("click", handleModalOutClick);

    return () => {
      window.removeEventListener("click", handleModalOutClick);
    };
  }, []);

  const handleOpenModal = () => {
    setIsOpen(true);
  };

  const handleCloseModal = () => {
    setIsOpen(false);
  };

  return (
    <ModalContext.Provider
      value={{ isOpen, handleOpenModal, handleCloseModal }}
    >
      {children}
    </ModalContext.Provider>
  );
};

export { ModalContext, ModalProvider };
