import { useContext } from "react";
import { ModalStyledContainer } from "./style";
import { ModalContext } from "../../../contexts/modal.context";
import type { IModalChildrenProps } from "../../../interfaces/modal.interface";
import { ModalBody } from "../ModalBody";

export const Modal = ({ children }: IModalChildrenProps) => {
  const { modalRef } = useContext(ModalContext);

  return (
    <ModalStyledContainer ref={modalRef}>
      <ModalBody>{children}</ModalBody>
    </ModalStyledContainer>
  );
};
