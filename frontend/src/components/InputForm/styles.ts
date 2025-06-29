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
    }

    label,
    input {
        font-family: var(--font-inter);
        font-size: var(--font-size-20);
    }

    input {
        border-radius: var(--border-radius-32);
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
        width: 100%;
        border: none;
        height: 56px;
        padding: 8px 20px;
        background-size: 24px 24px;
        font-size: 20px;
        font-weight: 700;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
        background-color: ${(props) => (props.error ? "var(--color-error-2)" : "var(--color-input-background)")};
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
