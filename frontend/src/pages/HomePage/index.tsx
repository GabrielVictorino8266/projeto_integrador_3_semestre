import { Button } from "@styles/Buttons";
import { useModal } from "@hooks/useModal";

const HomePage = () => {
  const { handleOpenModal, MODALCOMPONENTS, modalType } = useModal();

  const modalContent = modalType ? MODALCOMPONENTS[modalType] : null;

  return (
    <>
      {modalContent ? modalContent() : null}
      <Button
        onClick={() => {
          handleOpenModal("driverRegister");
        }}
      >
        ABRIR O MODAL
      </Button>
    </>
  );
};

export default HomePage;
