import { ModalStyledContainer } from "./style";
import type { IModalChildrenProps } from "../../../interfaces/modal.interface";
import { ModalBody } from "../ModalBody";
import { useModal } from "../../../hooks";

export const Modal = ({ children }: IModalChildrenProps) => {
  const { modalRef } = useModal();

  return (
    <ModalStyledContainer ref={modalRef}>
      <ModalBody>{children}</ModalBody>
    </ModalStyledContainer>
  );
};
