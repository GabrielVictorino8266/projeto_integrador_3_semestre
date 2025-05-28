import { css } from "@emotion/react";
import styled from "@emotion/styled";

const genericButton = css`
  width: 200px;
  height: 48px;
  border-radius: var(--border-radius-16);
  font-size: var(--font-size-20);
  font-weight: var(--font-weight-500);
  border: none;
`;

const Button = styled.button`
  ${genericButton}
`;

export { Button };
