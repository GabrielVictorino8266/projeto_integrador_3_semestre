import { StyledRegisterContainer, StyledRegisterFormContainer } from './styles';
import type { ReactNode } from 'react';

export interface IChildrenProp {
  children: ReactNode;
  title: string;
  icon: ReactNode;
}

const RegisterPageGeneric = ({ children, title, icon }: IChildrenProp) => {
  return (
    <>
      <StyledRegisterContainer>
        <div className={'title'}>
          <h1>
            <i>{icon}</i>
            {title}
          </h1>
        </div>

        <StyledRegisterFormContainer>{children}</StyledRegisterFormContainer>
      </StyledRegisterContainer>
    </>
  );
};

export { RegisterPageGeneric };
