import { useContext } from "react";
import { ModalContext } from "../contexts/modal.context";

const useModal = () => {
  const modalContext = useContext(ModalContext);
  return modalContext;
};

export { useModal };
