import { ModalStyledContainer } from './style';
import { ModalBody } from '../ModalBody';
import { useModal } from '@hooks/useModal';
import type { IGenericModalProps } from '@interfaces/modal.interface';
import { ModalHeader } from '../ModalHeader';
import { DriverDelete } from '../DriverDelete';
import { VehicleDeleted } from '../VehicleDelete';
import { TripDeleted } from '../TripDelete';

export const Modal = ({ type }: IGenericModalProps) => {
  const { modalRef } = useModal();

  return (
    <ModalStyledContainer ref={modalRef}>
      <ModalBody>
        {(() => {
          switch (type) {
            case 'driverDeleteConfirmation':
              return (
                <>
                  <ModalHeader modalTitle='CONFIRMAR EXCLUSÃO:' />
                  <DriverDelete />
                </>
              );
            case 'vehicleDeleteConfirmation':
              return (
                <>
                  <ModalHeader modalTitle='CONFIRMAR EXCLUSÃO:' />
                  <VehicleDeleted />
                </>
              );
            case 'tripDeleteConfirmation':
              return (
                <>
                  <ModalHeader modalTitle='CONFIRMAR EXLUSÃO:' />
                  <TripDeleted />
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
