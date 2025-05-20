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

const AvisoModalContent = () => {
  return (
    <Modal>
      <ModalHeader modalTitle={"AVISO"} />
      <p>AVISO</p>
      <input type="text" />
      <button>OK</button>
    </Modal>
  );
};

export { DriverRegisterModalContent, AvisoModalContent };
