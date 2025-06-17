import { forwardRef } from "react";
import Select from "react-select";

type Option = { value: string; label: string };

interface SelectStatusProps {
  options: Option[];                       
  value: string | null;                    
  onChange: (val: string | null) => void;
  placeholder?: string;
}

export const SelectStatus = forwardRef<any, SelectStatusProps>(
  ({ options, value, onChange, placeholder = "Selecionar..." }, ref) => {
    const selected = options.find((o) => o.value === value) || null;

    return (
      <Select<Option, false>
        ref={ref}
        options={options}
        value={selected}
        onChange={(opt) => onChange(opt?.value ?? null)}
        placeholder={placeholder}
        isSearchable
        styles={{
          control: (base) => ({
            ...base,
            borderRadius: "10px",
            padding: "4px 6px",
            border: "2px solid #ccc",
            boxShadow: "none",
            minWidth: "160px",
            cursor: "pointer",
          }),
          valueContainer: (base) => ({ ...base, cursor: "pointer" }),
          option: (base, s) => ({
            ...base,
            cursor: "pointer",
            backgroundColor: s.isFocused ? "#eee" : "white",
            color: "black",
          }),
          menu: (b) => ({
            ...b,
            borderRadius: "10px",
            boxShadow: "0 4px 12px rgba(0,0,0,.1)",
          }),
        }}
      />
    );
  }
);

SelectStatus.displayName = "SelectStatus";
