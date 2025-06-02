import { StyledRegisterContainer, StyledRegisterFormContainer } from "./styles";
import type { ReactNode } from "react";

export interface IChildrenProp {
  children: ReactNode;
  title: string
}

const RegisterPageGeneric = ({ children, title }: IChildrenProp) => {
  return (
    <>
      <StyledRegisterContainer>
        <div className={"title"}>
          <h1>{title}</h1>
        </div>

        <StyledRegisterFormContainer>{children}</StyledRegisterFormContainer>
      </StyledRegisterContainer>
    </>
  );
};

export { RegisterPageGeneric };
