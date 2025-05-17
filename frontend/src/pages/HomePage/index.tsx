import { useContext } from "react";
import { TestComponent } from "./style";
import { ModalContext } from "../../contexts/modal.context";
import { Modal } from "../../components/Modal/ModalGeneric";

const HomePage = () => {
  const { isOpen, handleOpenModal } = useContext(ModalContext);
  return (
    <>
      {isOpen ? <Modal /> : null}
      <TestComponent primary={false}>
        <button onClick={() => handleOpenModal()}>Abrir Modal</button>
      </TestComponent>
    </>
  );
};

export default HomePage;
