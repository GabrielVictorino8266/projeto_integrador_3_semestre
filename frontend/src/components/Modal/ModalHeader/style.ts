import styled from "@emotion/styled";

const ModalHeaderStyled = styled.section`
  width: 100%;
  height: 2rem;
  display: flex;
  flex-direction: row;
  border-bottom: 1px solid var(--color-brand-1);
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;

  p {
    font-weight: var(--font-weight-600);
  }
`;

export { ModalHeaderStyled };
