import type { IDefaultChildrenProp } from "@interfaces/default.interface";
import { StyledRegisterContainer, StyledRegisterFormContainer } from "./styles";

const RegisterPageGeneric = ({ children }: IDefaultChildrenProp) => {
  return (
    <>
      <StyledRegisterContainer>
        <div className={"title"}>
          <h1>Cadastro de motorista</h1>
        </div>

        <StyledRegisterFormContainer>{children}</StyledRegisterFormContainer>
      </StyledRegisterContainer>
    </>
  );
};

export { RegisterPageGeneric };
