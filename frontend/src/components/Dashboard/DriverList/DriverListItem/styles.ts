import styled from "@emotion/styled";

const StyledTableRow = styled.tr`
  text-align: center;

  button {
    background-color: transparent;
    border: none;

    .icon {
      width: 32px;
      height: 32px;
    }

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

    .driverActive {
      color: var(--colorStatus-maintenance);
    }
    .driverInactive {
      color: var(--colorStatus-unavailable);
    }
  }
`;

export { StyledTableRow };
