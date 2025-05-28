import styled from "@emotion/styled";

const StyledRegisterContainer = styled.div`
  margin: 0 auto;
  background-color: var(--color-white);

  .title {
    display: flex;
    align-items: center;
    padding: 16px 32px;

    h1 {
      font-size: var(--font-size-40);
      font-weight: var(--font-weight-800);
    }
  }
`;

const StyledRegisterFormContainer = styled.div`
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: rgba(191, 210, 236, 0.98);

  form {
    width: 100%;
    background-color: var(--color-brand-1);
    padding: 32px 16px;
    border-radius: 16px;
    max-width: 900px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .form__sendButton {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  @media (min-width: 768px) {
    form {
      flex-direction: row;
      flex-wrap: wrap;
      gap: 8px;
      justify-content: space-between;
      height: 600px;
      padding: 50px;
      fieldset {
        width: 47%;
        gap: 8px;
      }
    }
  }
`;

export { StyledRegisterContainer, StyledRegisterFormContainer };
