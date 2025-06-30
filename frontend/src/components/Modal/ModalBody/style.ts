import styled from '@emotion/styled';

const ModalBodyStyled = styled.section`
  width: 90%;
  max-width: 600px;
  height: min-content;
  background-color: #ffffff;
  border-radius: 8px;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 20px;

  .modal__title {
    display: flex;
    font-size: var(--font-size-20);
  }

  .closeButton {
    background-color: transparent;
    border-radius: 100%;
    width: 2rem;
    height: 2rem;
    border: none;
    font-size: var(--font-size-20);
    font-weight: var(--font-weight-600);
  }

  .warningMessage {
    color: var(--color-attention);
  }

  .modal_buttonsContainer {
    display: flex;
    flex-direction: row;
    width: 100%;
    align-items: end;
    gap: 16px;
    justify-content: end;
  }

  form {
    display: flex;
    flex-direction: column;
    background-color: var(--color-brand-1);
    padding: 16px;
    border-radius: 8px;
  }
`;

export { ModalBodyStyled };
