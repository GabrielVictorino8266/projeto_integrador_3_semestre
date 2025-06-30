import styled from '@emotion/styled';

const StyledDashboardHeader = styled.section`
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  height: 5rem;
  padding: 0 24px;

  background-color: var(--color-white);

  p {
    font-size: var(--font-size-40);
    font-weight: var(--font-weight-800);
    display: flex;
    gap: 16px;
  }
`;

export { StyledDashboardHeader };
