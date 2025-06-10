import { Button } from "@styles/Buttons";
import { useModal } from "@hooks/useModal";
import { Modal } from "@components/Modal/ModalGeneric";

const HomePage = () => {
  const { isOpen, modalType, handleOpenModal } = useModal();

  return (
    <>
      {isOpen && <Modal type={modalType} />}
      <Button
        onClick={() => {
          handleOpenModal({ modalType: "driverEdit" });
        }}
      >
        ABRIR O MODAL
      </Button>
    </>
  );
};

export default HomePage;
