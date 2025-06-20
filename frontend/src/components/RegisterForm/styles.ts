import styled from "@emotion/styled";

const StyledRegisterContainer = styled.div`
  margin: 0 auto;
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--color-white);

  .title {
    display: flex;
    align-items: center;
    padding: 16px 32px;

    h1 {
      font-size: var(--font-size-40);
      font-weight: var(--font-weight-800);
      display: flex;
      flex-direction: row;
      gap: 16px;
    }
  }
`;

const StyledRegisterFormContainer = styled.div`
  flex: 1;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: rgba(191, 210, 236, 0.98);
  overflow-y: auto;

  form {
    width: 100%;
    background-color: var(--color-white);
    padding: 32px 16px;
    border-radius: 16px;
    max-width: 900px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: auto;
    box-shadow: 8px 8px 16px rgba(0, 0, 0, 0.25);
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
      height: auto;
      padding: 50px;

      fieldset {
        width: 100%;
        gap: 8px;
      }
    }
  }
`;

export { StyledRegisterContainer, StyledRegisterFormContainer };
