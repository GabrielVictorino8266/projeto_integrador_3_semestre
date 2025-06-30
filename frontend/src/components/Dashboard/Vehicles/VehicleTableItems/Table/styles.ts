import styled from '@emotion/styled';

const StyledTableRow = styled.tr`
  text-align: center;

  button {
    background-color: transparent;
    border: none;

    .deleteButton {
      :hover {
        color: var(--color-error);
      }
    }

    .editButton {
      :hover {
        color: var(--color-brand-2);
      }
    }
  }
`;

export { StyledTableRow };
