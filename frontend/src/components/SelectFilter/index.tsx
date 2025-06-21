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
                    control: (base, state) => ({
                        ...base,
                        minHeight: "56px",
                        height: "56px",
                        borderRadius: "32px",
                        border: state.isFocused ? "2px solid var(--color-primary)" : "none",
                        boxShadow: "0 2px 4px rgba(0,0,0,0.25)",
                        backgroundColor: "#ffffff",
                        padding: "0 18px",
                        cursor: "pointer",
                    }),
                    valueContainer: (base) => ({
                        ...base,
                        padding: 0,
                        fontSize: "20px",
                        fontWeight: 700,
                    }),
                    placeholder: (base) => ({
                        ...base,
                        fontStyle: "italic",
                        fontWeight: 700,
                        color: "#7b7b7b",
                    }),
                    indicatorsContainer: (base) => ({
                        ...base,
                        color: "#7b7b7b",
                    }),
                    indicatorSeparator: () => ({ display: "none" }),
                    option: (base, state) => ({
                        ...base,
                        backgroundColor: state.isFocused ? "#eee" : "#fff",
                        color: "#000",
                        cursor: "pointer",
                        fontWeight: 600,
                    }),
                    menu: (base) => ({
                        ...base,
                        borderRadius: "10px",
                        boxShadow: "0 9px 22px rgba(18, 105, 0, 0.1)",
                    }),
                }}
            />
        );
    }
);

SelectStatus.displayName = "SelectStatus";
