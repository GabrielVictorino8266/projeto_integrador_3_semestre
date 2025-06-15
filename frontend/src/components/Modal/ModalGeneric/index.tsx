import { ModalStyledContainer } from "./style";
import { ModalBody } from "../ModalBody";
import { useModal } from "@hooks/useModal";
import type { IGenericModalProps } from "@interfaces/modal.interface";
import { ModalHeader } from "../ModalHeader";
import { DriverDelete } from "../DriverDelete";

export const Modal = ({ type }: IGenericModalProps) => {
  const { modalRef } = useModal();

  return (
    <ModalStyledContainer ref={modalRef}>
      <ModalBody>
        {(() => {
          switch (type) {
            case "driverDeleteConfirmation":
              return (
                <>
                  <ModalHeader modalTitle="CONFIRMAR DELEÇÃO:" />
                  <DriverDelete />
                </>
              );

            default:
              return <></>;
          }
        })()}
      </ModalBody>
    </ModalStyledContainer>
  );
};
