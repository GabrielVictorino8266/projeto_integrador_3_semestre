import { useEffect, useState } from "react";
import { useModal } from "@hooks/useModal";
import { DarkBlueButton, DeleteButton } from "@styles/Buttons";
import { useNavigate } from "react-router-dom";
import { deleteTrip } from "@services/Api/Trips/deleteTrip";
import { getTripForID } from "@services/Api/Trips/getTripForId";
import type { TripsIdResponse } from "@interfaces/trips.interface";

export const TripDeleted = () => {
    const { modalContentID, handleCloseModal } = useModal();
    const [trip, setTrip] = useState<TripsIdResponse | null>(null);
    const navigate = useNavigate();

    useEffect(() => {
        if (modalContentID) getTripForID(modalContentID).then(setTrip);
    }, [modalContentID]);

    return (
        <>
            <p>
                <strong>Viagem: {trip?.destination ?? "Carregando..."}</strong>
            </p>
            <p className="warningMessage">Esta ação não pode ser desfeita!</p>
            <div className="modal_buttonsContainer">
                <DeleteButton
                    onClick={async () => {
                        if (modalContentID) {
                            await deleteTrip(modalContentID!);
                            navigate(0);
                            handleCloseModal();
                        }
                    }}
                >
                    DELETAR
                </DeleteButton>
                <DarkBlueButton onClick={handleCloseModal}>Cancelar</DarkBlueButton>
            </div>
        </>
    );
};
