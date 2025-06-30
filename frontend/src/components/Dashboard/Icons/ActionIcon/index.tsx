import { FiTrash2 } from 'react-icons/fi';
import { TbEdit } from 'react-icons/tb';
import { ButtonIconContainer } from './styles';

type iconType = 'edit' | 'delete';
interface ITypeOptionProp {
  type: iconType;
}

const ActionIcon = ({ type }: ITypeOptionProp) => {
  return (
    <ButtonIconContainer>
      {(() => {
        switch (type) {
          case 'edit':
            return <TbEdit className='icon edit' />;

          case 'delete':
            return <FiTrash2 className='icon delete' />;
        }
      })()}
    </ButtonIconContainer>
  );
};

export { ActionIcon };
