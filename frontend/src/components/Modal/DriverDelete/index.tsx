import { useModal } from "@hooks/useModal";
import { DarkBlueButton, DeleteButton } from "@styles/Buttons";

const DriverDelete = () => {
  const { modalContentID, handleCloseModal } = useModal();

  /*   {
    lógica de deleltar
  } */

  return (
    <>
      <p>
        <strong>ID do usuário: {modalContentID}</strong>
      </p>
      <p className="warningMessage">Esta ação não pode ser desfeita!</p>
      <div className="modal_buttonsContainer">
        <DeleteButton>DELETAR</DeleteButton>
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
