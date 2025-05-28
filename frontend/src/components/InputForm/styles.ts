import styled from "@emotion/styled";
import type { FieldError } from "react-hook-form";

interface StyledInputContainerProps {
  error?: FieldError;
}

const StyledInput = styled.fieldset<StyledInputContainerProps>`
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 4px;

  label {
    font-weight: var(--font-weight-700);
    color: var(--color-white);
  }

  label,
  input {
    font-family: var(--font-inter);
    font-size: var(--font-size-20);
  }

  input {
    border-radius: var(--border-radius-16);
    width: 100%;
    height: 3rem;
    padding: 8px 20px;
    background-color: ${(props) =>
      props.error ? "var(--color-error-2)" : "var(--color-white)"};
  }

  .inputErrorMessage {
    color: var(--color-error);
    font-weight: 500;
    font-size: var(--font-size-12);
  }

  p {
    height: 12px;
  }
`;

export { StyledInput };
