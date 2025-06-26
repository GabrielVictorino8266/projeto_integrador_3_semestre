import { useEffect, useState } from "react";
import { useModal } from "@hooks/useModal";
import { getVehiclesId } from "@services/Api/Vehicles/GetVehiclesId";
import { BorderedButton, DeleteButton } from "@styles/Buttons";
import type { DataProps } from "@schemas/CadsVeiculos";
import { DeleteVehicle } from "@services/Api/Vehicles/DeleteVehicle";
import { useNavigate } from "react-router-dom";

const VehicleDeleted = () => {
  const { modalContentID, handleCloseModal } = useModal();
  const [vehicle, setVehicle] = useState<DataProps | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (modalContentID) getVehiclesId(modalContentID).then(setVehicle);
  }, [modalContentID]);

  return (
    <>
      <p>
        <strong>
          Plca do veículo: {vehicle?.licensePlate ?? "Carregando..."}
        </strong>
      </p>
      <p className="warningMessage">Esta ação não pode ser desfeita!</p>
      <div className="modal_buttonsContainer">
        <BorderedButton onClick={handleCloseModal}>Cancelar</BorderedButton>
        <DeleteButton
          onClick={async () => {
            if (modalContentID) {
              await DeleteVehicle(modalContentID!);
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
};

export { VehicleDeleted };
