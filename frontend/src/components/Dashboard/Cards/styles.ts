import styled from "@emotion/styled";

const StyledCardWithRightBorder = styled.div`
  background-color: var(--color-white);
  height: 300px;
  min-height: 10rem;
  width: 30rem;
  border-left: 8px solid var(--color-brand-2);
  border-radius: 0 15px 15px 0;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 32px;

  .card__text {
    font-size: var(--font-size-20);
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .card__number {
    font-size: var(--font-size-36);
    font-weight: var(--font-weight-800);
  }

  .card__values {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
`;

export { StyledCardWithRightBorder };
