import { useDriver } from "@hooks/useDriver";
import { useModal } from "@hooks/useModal";
import { DarkBlueButton, DeleteButton } from "@styles/Buttons";

const DriverDelete = () => {
  const { modalContentID, handleCloseModal } = useModal();
  const { deleteDriver } = useDriver();

  return (
    <>
      <p>
        <strong>ID do usuário: {modalContentID}</strong>
      </p>
      <p className="warningMessage">Esta ação não pode ser desfeita!</p>
      <div className="modal_buttonsContainer">
        <DeleteButton
          onClick={() => {
            deleteDriver(modalContentID!);
          }}
        >
          DELETAR
        </DeleteButton>
        <DarkBlueButton
          onClick={() => {
            handleCloseModal();
          }}
        >
          Cancelar
        </DarkBlueButton>
      </div>
    </>
  );
};

export { DriverDelete };
