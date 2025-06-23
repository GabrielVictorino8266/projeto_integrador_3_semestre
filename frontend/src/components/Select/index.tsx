import type { SelectHTMLAttributes } from "react";
import type { FieldError } from "react-hook-form";
import { StyledSelectFieldSet } from "./styles";

interface ISelectOptions {
  value: string;
  label: string;
}

interface IFormSelectSet extends SelectHTMLAttributes<HTMLSelectElement> {
  optionsArray: Array<ISelectOptions>;
  label?: string;
  error: FieldError | undefined;
}

const SelectInputForm = ({
  optionsArray,
  label,
  error,
  ...rest
}: IFormSelectSet) => {
  const selectOptions = optionsArray.map((element: ISelectOptions) => {
    return (
      <option key={element.value} value={element.value}>
        {element.label}
      </option>
    );
  });
  return (
    <>
      <StyledSelectFieldSet error={error}>
        <label>{label}</label>
        <select id="" {...rest}>
          <option value="">Selecione um tipo</option>
          {selectOptions}
        </select>
        {error ? <p className="inputErrorMessage">{error.message}</p> : <p></p>}
      </StyledSelectFieldSet>
    </>
  );
};

export { SelectInputForm };
