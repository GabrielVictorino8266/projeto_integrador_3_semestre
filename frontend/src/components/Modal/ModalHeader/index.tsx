import { ModalHeaderStyled } from './style';
import { useModal } from '@hooks/useModal';

interface IModalTitle {
  modalTitle: string;
}

const ModalHeader = ({ modalTitle }: IModalTitle) => {
  const { handleCloseModal } = useModal();

  return (
    <ModalHeaderStyled>
      <p className='modal__title'>{modalTitle}</p>
      <button
        className='closeButton'
        onClick={() => {
          handleCloseModal();
        }}
      >
        X
      </button>
    </ModalHeaderStyled>
  );
};

export { ModalHeader };
