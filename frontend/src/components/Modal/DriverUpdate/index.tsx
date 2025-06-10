import { RegInput } from "@components/InputForm";
import { useModal } from "@hooks/useModal";
import { DarkBlueButton } from "@styles/Buttons";

const DriverUpdate = () => {
  const { modalContentID, handleCloseModal } = useModal();

  return (
    <>
      <p>
        <strong>ID do usuário: {modalContentID}</strong>
      </p>

      <form>
        <RegInput type={""} placeholder={""} id={""} label={""} />
      </form>
      <div className="modal_buttonsContainer">
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

export { DriverUpdate };
