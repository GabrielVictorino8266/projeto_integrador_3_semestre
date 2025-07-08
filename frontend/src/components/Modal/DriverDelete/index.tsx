import { useDriver } from '@hooks/useDriver';
import { useModal } from '@hooks/useModal';
import { BorderedButton, DeleteButton } from '@styles/Buttons';

const DriverDelete = () => {
  const { modalContentID, handleCloseModal } = useModal();
  const { deleteDriver } = useDriver();

  return (
    <>
      <p>
        <strong>
          Tem certeza que deseja realizar a exclusão do motorista?
        </strong>
      </p>
      <p className='warningMessage'>
        <strong>Esta ação não pode ser desfeita!</strong>
      </p>
      <div className='modal_buttonsContainer'>
        <BorderedButton
          onClick={() => {
            handleCloseModal();
          }}
        >
          Cancelar
        </BorderedButton>
        <DeleteButton
          onClick={() => {
            deleteDriver(modalContentID!);
          }}
        >
          DELETAR
        </DeleteButton>
      </div>
    </>
  );
};

export { DriverDelete };
