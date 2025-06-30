import { useEffect, useState } from 'react';
import { useModal } from '@hooks/useModal';
import { BorderedButton, DeleteButton } from '@styles/Buttons';
import { useNavigate } from 'react-router-dom';
import { deleteTrip } from '@services/Api/Trips/deleteTrip';
import type { TripsIdResponse } from '@interfaces/trips.interface';
import { getTripForID } from '@services/Api/Trips/getTripForId';

export function TripDeleted() {
  const { modalContentID, handleCloseModal } = useModal();
  const [trip, setTrip] = useState<TripsIdResponse | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (modalContentID) getTripForID(modalContentID).then(setTrip);
  }, [modalContentID]);

  return (
    <>
      <p>
        <strong>
          Excluir a viagem para:{' '}
          <span style={{ color: '#0057D9' }}>{trip?.destination}</span> ?
        </strong>
      </p>
      <p className='warningMessage'>
        <strong>Esta ação não pode ser desfeita!</strong>
      </p>
      <div className='modal_buttonsContainer'>
        <BorderedButton
          onClick={() => {
            handleCloseModal();
          }}
        >
          Cancelar
        </BorderedButton>
        <DeleteButton
          onClick={() => {
            if (modalContentID) {
              deleteTrip(modalContentID!);
              navigate(0);
              handleCloseModal();
            }
          }}
        >
          DELETAR
        </DeleteButton>
      </div>
    </>
  );
}
