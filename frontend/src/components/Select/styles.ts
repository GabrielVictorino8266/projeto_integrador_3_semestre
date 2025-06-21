import styled from "@emotion/styled";

interface FieldProps {
  error?: unknown;
}

export const StyledSelectFieldSet = styled.fieldset<FieldProps>`
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 5px;
  width: 100%;
  margin-bottom: 2%;
  border: none;
  padding: 0;
  position: relative;

  label {
    font-size: 20px;
    font-weight: var(--font-weight-700);
  }

  select {
    width: 100%;
    height: 56px;
    border: none;
    border-radius: 32px;
    background: ${(p) => (p.error ? "var(--color-error-2)" : "#f2f2f2")};
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
    font-size: 20px;
    font-weight: 700;
    padding: 0 50px 0 24px;
    color: #000;
    cursor: pointer;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    position: relative;
  }

  &::after {
    content: "▼";
    position: absolute;
    right: 18px;
    top: calc(50% + 8px);
    transform: translateY(-50%);
    pointer-events: none;
    font-size: 16px;
    color: #7b7b7b;
  }

  .inputErrorMessage {
    font-size: var(--font-size-12);
    color: var(--color-error);
    font-weight: 500;
    line-height: 80%;
  }
`;
