import type { IDefaultChildrenProp } from '@interfaces/default.interface';
import { StyledCardWithRightBorder } from './styles';

const CardWithRightBorder = ({ children }: IDefaultChildrenProp) => {
  return <StyledCardWithRightBorder>{children}</StyledCardWithRightBorder>;
};

export { CardWithRightBorder };
