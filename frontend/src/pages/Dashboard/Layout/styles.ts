import styled from "@emotion/styled";

const Main = styled.main`
  display: flex;
  width: 100%;

  .dashboardItems_container {
    width: 100%;
    background-color: var(--color-background-dashboard);
  }

  .dashboard__details {
    height: 100%;
    width: 100%;
    padding: 12px 0;

    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .cards__container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }

  table {
    width: 100%;
    background-color: var(--color-white);
    border-radius: var(--border-radius-8);
  }

  td {
    align-content: center;
  }

  th {
    align-content: center;
    border-bottom: 1px solid black;
  }

  tr {
    text-align: center;
    border-bottom: 1px solid black;
    height: 3rem;
    align-content: center;
  }

  tr:last-of-type {
    border-bottom: none;
  }

  thead > tr > th {
    height: 2rem;
    font-size: var(--font-size-18);
  }

  .list__title {
    font-size: var(--font-size-20);
    margin-bottom: 8px;
  }
`;
export { Main };
