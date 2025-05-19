import { useContext } from "react";
import { Modal } from "../../components/Modal/ModalGeneric";
import { ModalContext } from "../../contexts/modal.context";

const HomePage = () => {
  const { isOpen, handleOpenModal } = useContext(ModalContext);
  return (
    <>
      {isOpen ? <Modal /> : null}
      <button
        onClick={() => {
          handleOpenModal();
        }}
      >
        Abrir o modal
      </button>
    </>
  );
};

export default HomePage;
