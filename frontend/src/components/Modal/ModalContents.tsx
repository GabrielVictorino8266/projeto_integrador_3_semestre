import { Modal } from "./ModalGeneric";
import { ModalHeader } from "./ModalHeader";

const DriverRegisterModalContent = () => {
  return (
    <Modal>
      <ModalHeader modalTitle={"Cadastrar Motorista"} />
      <p>Formulario</p>
      <input type="text" />
      <button>Enviar</button>
    </Modal>
  );
};

export { DriverRegisterModalContent };
