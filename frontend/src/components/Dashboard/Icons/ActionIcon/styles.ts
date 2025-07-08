import styled from '@emotion/styled';

const ButtonIconContainer = styled.i`
  .icon {
    width: 32px;
    height: 32px;
  }

  .edit {
    :hover {
      color: var(--color-edit);
    }
  }

  .delete {
    :hover {
      color: var(--color-delete);
    }
  }
`;

export { ButtonIconContainer };
