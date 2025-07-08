import type { IModalChildrenProps } from '@interfaces/modal.interface';
import { ModalBodyStyled } from './style';

const ModalBody = ({ children }: IModalChildrenProps) => {
  return <ModalBodyStyled>{children}</ModalBodyStyled>;
};

export { ModalBody };
