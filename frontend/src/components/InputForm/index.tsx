import { forwardRef } from "react";
import { StyledInput } from "./styles";
import type { FieldError } from "react-hook-form";

interface IInput {
  type: string;
  placeholder: string;
  id: string;
  label: string;
  error?: FieldError;
}

const RegInput = forwardRef<HTMLInputElement, IInput>(
  ({ type, placeholder, id, label, error, ...rest }, ref) => {
    return (
      <StyledInput error={error}>
        <label htmlFor={id}>{label}</label>
        <input
          type={type}
          placeholder={placeholder}
          id={id}
          ref={ref}
          {...rest}
        />
        {error ? <p className="inputErrorMessage">{error.message}</p> : <p></p>}
      </StyledInput>
    );
  }
);

export { RegInput };
