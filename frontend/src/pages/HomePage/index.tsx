import { useModal } from "../../hooks";

const HomePage = () => {
  const { handleOpenModal, MODALCOMPONENTS, modalType } = useModal();

  const modalContent = modalType ? MODALCOMPONENTS[modalType] : null;
  console.log(modalContent);

  return (
    <>
      {modalContent ? modalContent() : null}
      <button
        onClick={() => {
          handleOpenModal("driverRegister");
        }}
      >
        Abrir o registro
      </button>
    </>
  );
};

export default HomePage;
