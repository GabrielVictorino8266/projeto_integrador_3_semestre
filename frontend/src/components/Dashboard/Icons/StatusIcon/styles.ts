import styled from '@emotion/styled';

const IconContainer = styled.i`
  .iconSize {
    width: 32px;
    height: 32px;
  }
  .red {
    color: var(--colorStatus-unavailable);
  }
  .blue {
    color: var(--colorStatus-maintenance);
  }

  .green {
    color: var(--colorStatus-available);
  }

  .orange {
    color: #ca8a29;
  }

  .yallow {
    color: #ffc107;
  }

  .blueTrip {
    color: #17a2b8;
  }

  .greenTrip {
    color: #28a745;
  }
`;

export { IconContainer };
